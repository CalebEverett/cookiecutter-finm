from pathlib import Path

from git import Repo

DOTENV_PATH = "{{cookiecutter.dotenv_path}}"
INIT_REPO = "{{cookiecutter.init_repo}}" == "yes"
PUSH_TO_REMOTE = "{{cookiecutter.merge_remote}}" == "yes"

BASE_URL = "https://api.github.com"
REPO_NAME = "{{cookiecutter.repo_name}}"

if DOTENV_PATH:
    Path(".env").write_text(Path(DOTENV_PATH).read_text())

if INIT_REPO:
    repo = Repo.init()
    repo.git.add(all=True)
    repo.index.commit("Add initial project skeleton.")

if PUSH_TO_REMOTE:
    repo.create_remote("origin", url="git@github.com:{{ cookiecutter.repo_name }}.git")
    remote = repo.remote("origin")
    remote.push(refspec="master:master")
