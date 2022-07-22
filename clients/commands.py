import click


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new Client"""
    pass

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass

@clients.command()
@click.pass_context
def update(ctx):
    """Update client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx):
    """Delete client"""
    pass


all = clients







