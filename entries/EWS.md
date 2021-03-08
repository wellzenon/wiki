PowerShell function using EWS (OAuth2) to perform these operations against Exchange Online Mailboxes.

## Table of Contents

- [Functions](#functions)
- [Requirements](#requirements)
- [How To Install The Module](#how-to-install-the-module)
- [How To Uninstall The Module](#how-to-uninstall-the-module)
- [OAuth Access Token Requirement](#oauth-access-token-requirement)
- [Usage Examples](#usage-examples)

## Functions

So far there are two functions included in this module.

- [`Get-EwsFolder`](docs/Get-EwsFolder.md)
  * List ALL folders from a mailbox
  * Search a folder from mailbox by folder display name (eg. `Inbox`, `Drafts`)
  * Get a folder from mailbox by folder ID (eg. `AQMkADRmZTI3MW..`)
- [`Move-EwsItem`](docs/Move-EwsItem.md)
  * Move all mailbox items from one folder to another
  * Move mailbox items between dates from one folder to another

## Requirements

- A registered Azure AD app
  * **API Name:** *Exchange*
  * **API Permission Type:** *Application*
  * **API Permission Name:** *full_access_as_app*

- Windows PowerShell 5.1
- [Exchange Web Services Managed API 2.2](https://www.microsoft.com/en-us/download/details.aspx?id=42951)
- For getting access tokens, you can have either [MSAL.PS](https://www.powershellgallery.com/packages/MSAL.PS) or [ADAL.PS](https://www.powershellgallery.com/packages/ADAL.PS)