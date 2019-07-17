workflow "Build and Test" {
  on = "push"
  resolves = [
    "Run",
  ]
}

action "Build" {
  uses = "jefftriplett/python-actions@master"
  args = "pip install -r requirements.txt"
}

action "Run" {
  uses = "jefftriplett/python-actions@master"
  args = "./test/testRun.sh"
  needs = ["Build"]
}
