terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }

  required_version = ">= 1.5.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "securecloud" {
  name     = "securecloud-rg"
  location = "West Europe"

  tags = {
    project     = "SecureCloud"
    environment = "dev"
    managed_by  = "terraform"
  }
}

resource "azurerm_container_registry" "securecloud" {
  name                = "securecloudacr2026"
  resource_group_name = azurerm_resource_group.securecloud.name
  location            = "Germany West Central"
  sku                 = "Basic"
  admin_enabled       = false

  tags = {
    project     = "SecureCloud"
    environment = "dev"
    managed_by  = "terraform"
  }
}