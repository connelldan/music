terraform {
  backend "gcs" {
    bucket  = "terraform-state-music-app"
    prefix  = "terraform/state"
  }
}

terraform {
  required_version = ">= 0.12"

  required_providers {
    google-beta = "= 3.35.0"
}
}
provider "google" {
  project     = var.gcp_project
  region      = var.gcp_region
}

provider "google-beta" {
  project     = var.gcp_project
  region      = var.gcp_region
}

