"""Container tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

from . import packages


# %% TASKS

@task
def get_sha(ctx: Context) -> str:
    """Get the latest commit sha from GitHub."""
    return ctx.run("git rev-parse HEAD", hide=True).stdout.strip()
    

@task
def compose(ctx: Context) -> None:
    """Start up docker compose."""
    ctx.run("docker compose up")


@task(pre=[packages.build])
def build(ctx: Context) -> None:
    """Build the container image."""
    tag = get_sha(ctx)
    ctx.run(f"docker build --tag={ctx.project.repository}:{tag} .")


@task
def run(ctx: Context) -> None:
    """Run the container image."""
    tag = get_sha(ctx)
    ctx.run(f"docker run --rm {ctx.project.repository}:{tag}")


@task(pre=[build, run], default=True)
def all(_: Context) -> None:
    """Run all container tasks."""