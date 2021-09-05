resource "google_project_iam_member" "compute_viewer_binding" {
  project = "${var.project_id}"
  role    = "roles/compute.viewer"
  member  = "serviceAccount:${google_service_account.ansible_service_account.email}"
}


  resource "google_service_account" "ansible_service_account" {
    account_id   = "ansible"
    display_name = "A service account for ansible dynamic inventory"
}
