from pathlib import Path

from git import Repo

DOTENV_PATH = "{{cookiecutter.dotenv_path}}"
INIT_REPO = "{{cookiecutter.init_repo}}" == "yes"
PUSH_REPO = "{{cookiecutter.push_repo}}" == "yes"

REPO_NAME = "{{cookiecutter.repo_name}}"

if DOTENV_PATH:
    Path(".env").write_text(Path(DOTENV_PATH).read_text())

if INIT_REPO:
    repo = Repo.init()
    repo.git.add(all=True)
    repo.index.commit("Add initial project skeleton.")
    repo.create_remote("origin", url="git@github.com:{{ cookiecutter.repo_name }}.git")

if PUSH_REPO:
    remote = repo.remote("origin")
    remote.push(refspec="master:master")
