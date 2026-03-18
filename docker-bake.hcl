target "build" {
  dockerfile = "Dockerfile"
  context = "."
}

target "validate-build" {
  inherits = ["build"]
  call = "check"
}