resource "google_compute_address" "application_address" {
  name         = "application-address"
  region       = "${var.region}"
}

resource "google_compute_instance" "application_production" {
  name = "application-production"
  machine_type = "f1-micro"
  zone = "${var.region}-a"
  labels = {
    "environment" = "production"
    "service" = "application"
  }

  boot_disk {
    initialize_params {
      size = 15
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "${var.network}"
    access_config {
      nat_ip = "${google_compute_address.application_address.address}"
    }

  }
  metadata = {
    ssh-keys = "serveruser:${file("pub_keys/sgmakarov.pub")}"
  }

  service_account {
    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    email = google_service_account.instance_mgr.email
    scopes = ["cloud-platform"]
  }
}
