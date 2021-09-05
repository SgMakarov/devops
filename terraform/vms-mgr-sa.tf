resource "google_service_account" "instance_mgr" {
  account_id   = "gcloud-instance-mgr-account"
  display_name = "instance manager"
}
