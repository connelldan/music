# define GCP region
variable "gcp_region" {
  type        = string
  description = "us-central1"
}
# define GCP project name
variable "gcp_project" {
  type        = string
  description = "disco-alchemy-242715"
}
# GCP authentication file
variable "gcp_auth_file" {
  type        = string
  description = "~/.service-accounts/terraform-admin.json"
}
variable "bucket_name" {
  type        = string
  description = "terraform-state-music-app"
}
variable "storage_class" {
  type        = string
  description = "REGIONAL"
}
