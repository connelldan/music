# Create a GCS Bucket
resource "google_storage_bucket" "state_bucket" {
  project       = var.gcp_project
  name          = var.bucket_name
  location      = var.gcp_region
  force_destroy = false
  storage_class = var.storage_class
  labels        = {}
  bucket_policy_only = false
  default_event_based_hold = false
  versioning {
    enabled = true
  }
}
