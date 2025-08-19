package com.Inventory.InventoryManagement.controller;

import com.Inventory.InventoryManagement.model.Product;
import com.Inventory.InventoryManagement.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/inventory/products")
public class ProductController {

    @Autowired
    private ProductRepository productRepository;

    // ✅ Get all products
    @GetMapping
    public List<Product> getAllProducts() {
        return productRepository.findAll();
    }

    // ✅ Get product by ID
    @GetMapping("/{id}")
    public ResponseEntity<?> getProductById(@PathVariable Long id) {
        return productRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // ✅ Add new product (with unique constraint handling)
    @PostMapping
    public ResponseEntity<?> addProduct(@RequestBody Product product) {
        try {
            Product savedProduct = productRepository.save(product);
            return ResponseEntity.ok(savedProduct);
        } catch (DataIntegrityViolationException ex) {
            return ResponseEntity.badRequest().body("Product name already exists.");
        }
    }

    // ✅ Update product
    @PutMapping("/{id}")
    public ResponseEntity<?> updateProduct(@PathVariable Long id, @RequestBody Product updatedProduct) {
        return productRepository.findById(id)
                .map(product -> {
                    product.setName(updatedProduct.getName());
                    product.setQuantity(updatedProduct.getQuantity());
                    try {
                        productRepository.save(product);
                        return ResponseEntity.ok(product);
                    } catch (DataIntegrityViolationException ex) {
                        return ResponseEntity.badRequest().body("Product name already exists.");
                    }
                })
                .orElse(ResponseEntity.notFound().build());
    }

    // ✅ Delete product
    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteProduct(@PathVariable Long id) {
        if (productRepository.existsById(id)) {
            productRepository.deleteById(id);
            return ResponseEntity.ok().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    // ✅ Add stock
    @PutMapping("/{id}/add-stock")
    public ResponseEntity<?> addStock(@PathVariable Long id, @RequestBody Integer request) {
        try {
            Integer quantityToAdd = request;
            Optional<Product> productOptional = productRepository.findById(id);

            if (!productOptional.isPresent()) {
                return ResponseEntity.notFound().build();
            }

            Product product = productOptional.get();
            if (quantityToAdd <= 0) {
                return ResponseEntity.badRequest().body("Quantity to add must be greater than 0");
            }

            int currentQuantity = product.getQuantity();
            product.setQuantity(currentQuantity + quantityToAdd);

            Product savedProduct = productRepository.save(product);
            return ResponseEntity.ok(savedProduct);

        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error adding stock: " + e.getMessage());
        }
    }

    // ✅ Order product
    @PutMapping("/{id}/order")
    public ResponseEntity<?> orderProduct(@PathVariable Long id, @RequestBody Integer orderedQuantity) {
        try {
            Optional<Product> productOptional = productRepository.findById(id);

            if (!productOptional.isPresent()) {
                return ResponseEntity.notFound().build();
            }

            Product product = productOptional.get();
            int currentQuantity = product.getQuantity();

            if (orderedQuantity <= 0) {
                return ResponseEntity.badRequest().body("ordered quantity must be greater than 0");
            }

            if (currentQuantity >= orderedQuantity) {
                product.setQuantity(currentQuantity - orderedQuantity);
                productRepository.save(product);

                Map<String, Object> response = new HashMap<>();
                response.put("ordered_quantity", orderedQuantity);
                response.put("deliver_quantity", orderedQuantity);
                response.put("remaining_quantity", product.getQuantity());

                return ResponseEntity.ok(response);
            } else {
                product.setQuantity(0);
                productRepository.save(product);

                Map<String, Object> response = new HashMap<>();
                response.put("ordered_quantity", orderedQuantity);
                response.put("deliver_quantity", currentQuantity);
                response.put("remaining_quantity", product.getQuantity());

                return ResponseEntity.ok(response);
            }

        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error processing order: " + e.getMessage());
        }
    }

    // ✅ Get stock of a product
    @GetMapping("/{id}/stock")
    public ResponseEntity<?> stockProduct(@PathVariable Long id) {
        return productRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
