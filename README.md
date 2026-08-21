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

- Python
- FastAPI
- Microsoft Entra ID
- SCIM 2.0
- REST APIs
- Cloudflare Tunnel
