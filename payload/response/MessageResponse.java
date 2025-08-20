package com.hashedin.huspark.payload.response;

import lombok.Data;
import lombok.RequiredArgsConstructor;

@Data
@RequiredArgsConstructor
public class MessageResponse {
    private final String message;
}