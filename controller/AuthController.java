package com.hashedin.huspark.controller;

import com.hashedin.huspark.model.Role;
import com.hashedin.huspark.model.User;
import com.hashedin.huspark.payload.request.LoginRequest;
import com.hashedin.huspark.payload.request.SignupRequest;
import com.hashedin.huspark.payload.response.JwtResponse;
import com.hashedin.huspark.payload.response.MessageResponse;
import com.hashedin.huspark.repository.UserRepository;
import com.hashedin.huspark.security.jwt.JwtUtils;
import com.hashedin.huspark.security.services.UserDetailsImpl;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@CrossOrigin(origins = "*", maxAge = 3600)
@RestController
@RequestMapping("/api/auth")
@Tag(name = "Authentication", description = "Endpoints for user registration and login")
public class AuthController {
    private final AuthenticationManager authenticationManager;
    private final UserRepository userRepository;
    private final PasswordEncoder encoder;
    private final JwtUtils jwtUtils;
    private static final Logger logger = LoggerFactory.getLogger(AuthController.class);

    public AuthController(AuthenticationManager authenticationManager, UserRepository userRepository,
                          PasswordEncoder encoder, JwtUtils jwtUtils) {
        this.authenticationManager = authenticationManager;
        this.userRepository = userRepository;
        this.encoder = encoder;
        this.jwtUtils = jwtUtils;
    }

    @Operation(summary = "Authenticate and login a user")
    @PostMapping("/signin")
    public ResponseEntity<?> authenticateUser(@Valid @RequestBody LoginRequest loginRequest) {
        // Log the received credentials for debugging purposes
        logger.info("Attempting to sign in with username: {}", loginRequest.getUsername());

        try {
            Authentication authentication = authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword()));

            SecurityContextHolder.getContext().setAuthentication(authentication);
            String jwt = jwtUtils.generateJwtToken(authentication);

            UserDetailsImpl userDetails = (UserDetailsImpl) authentication.getPrincipal();
            List<String> roles = userDetails.getAuthorities().stream()
                    .map(item -> item.getAuthority())
                    .collect(Collectors.toList());

            return ResponseEntity.ok(new JwtResponse(jwt,
                    userDetails.getId(),
                    userDetails.getUsername(),
                    userDetails.getEmail(),
                    roles));
        } catch (AuthenticationException e) {
            // Log the detailed authentication error
            logger.error("Authentication failed for username {}: {}", loginRequest.getUsername(), e.getMessage());
            return ResponseEntity
                    .status(401) // Use 401 for authentication failures
                    .body(new MessageResponse("Error: Invalid username or password."));
        }
    }

    @Operation(summary = "Register a new user")
    @PostMapping("/signup")
    public ResponseEntity<?> registerUser(@Valid @RequestBody SignupRequest signUpRequest) {
        if (userRepository.existsByUsername(signUpRequest.getUsername())) {
            return ResponseEntity
                    .badRequest()
                    .body(new MessageResponse("Error: Username is already taken!"));
        }

        if (userRepository.existsByEmail(signUpRequest.getEmail())) {
            return ResponseEntity
                    .badRequest()
                    .body(new MessageResponse("Error: Email is already in use!"));
        }

        Set<Role> roles = new HashSet<>();
        if (signUpRequest.getRole() != null) {
            switch (signUpRequest.getRole()) {
                case "admin":
                    roles.add(Role.ADMIN);
                    break;
                case "librarian":
                    roles.add(Role.LIBRARIAN);
                    break;
                default:
                    roles.add(Role.MEMBER);
            }
        } else {
            roles.add(Role.MEMBER);
        }

        User user = new User(signUpRequest.getUsername(),
                signUpRequest.getEmail(),
                encoder.encode(signUpRequest.getPassword()),
                roles);
        userRepository.save(user);

        return ResponseEntity.ok(new MessageResponse("User registered successfully!"));
    }
}