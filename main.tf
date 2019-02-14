provider "aws" {
  region = "${var.aws-region}"
  profile = "greka"
  access_key = "${var.access-key}"
  secret_key = "${var.secret-key}"
}

resource "aws_instance" "test-vm-t2-micro" {

  ami = "ami-03b62c561f2175e22"
  instance_type = "t2.micro"
  key_name = "${var.aws-key-name}"
  associate_public_ip_address = "true"
  subnet_id = "subnet-a7d8e8cf"
  tags {
    "Name"      = "test-vm-t2-micro"
  }
}

