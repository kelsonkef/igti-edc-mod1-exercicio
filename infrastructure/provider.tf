provider "aws" {
    region = "us-east-2"
  
}

# Centraliza o arquivo de controle de estado do terraform
# Não conseguimos utilizar variveis e o buckter precisar está criado
terraform {
  backend "s3" {
      bucket = "terraform-state-igti-kelson"
      key = "state/igti/edc/mod1/terraform.tfstate"
      region = "us-east-2"

    
  }
}