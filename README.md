# Custom SCIM 2.0 Identity Provisioning Lab

## Overview

Built a custom SCIM 2.0 identity provisioning service using Python and FastAPI, integrated with Microsoft Entra ID to automate identity lifecycle management for a custom CRM application.

## Architecture

Microsoft Entra ID
        |
        | SCIM 2.0
        v
Cloudflare Tunnel
        |
        v
FastAPI / Python
        |
        v
Knotrah CRM

## Implemented

- SCIM 2.0 user provisioning
- User identity matching
- Attribute mapping from Microsoft Entra ID
- User updates and lifecycle changes
- Group provisioning
- SCIM User and Group REST endpoints
- Automated provisioning through Microsoft Entra ID
- Secure external connectivity using Cloudflare Tunnel

## Testing & Troubleshooting

Validated the integration through Microsoft Entra provisioning tests and FastAPI API testing.

Troubleshot and resolved:
- HTTP 405 Method Not Allowed responses
- SCIM user matching failures
- SCIM response deserialization errors
- Provisioning and deprovisioning scope behavior

## Technologies



## Screenshots

### Microsoft Entra ID Provisioning

This screenshot shows the successful user provisioning workflow between Microsoft Entra ID and the custom SCIM service. The user was assigned through group-based application assignment, evaluated as in scope, matched between the source and target system, and successfully provisioned through the SCIM integration.

### FastAPI SCIM Endpoints

This screenshot shows the FastAPI documentation for the implemented SCIM 2.0 endpoints. These endpoints allow Microsoft Entra ID to communicate with the custom identity service to perform user lifecycle operations, including creating, retrieving, and updating users and groups.

### API / Terminal Logs

This screenshot shows the FastAPI server logs during SCIM provisioning tests. The logs were used to validate communication between Microsoft Entra ID and the SCIM service, monitor API requests, and troubleshoot integration issues by analyzing HTTP responses and status codes.

- Python
- FastAPI
- Microsoft Entra ID
- SCIM 2.0
- REST APIs
- Cloudflare Tunnel
