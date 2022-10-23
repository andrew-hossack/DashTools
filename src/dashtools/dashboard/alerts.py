import dash_mantine_components as dmc
from dash_iconify import DashIconify

# NOTIFICATION_DURATION_SECONDS = 8


def render(key: str):
    if key == 'FileNotFoundError':
        return dmc.Notification(
            message="The file path you provided does not exist. Please check your filepath and try again.",
            title="Warning",
            color='red',
            icon=[DashIconify(icon="ep:warning")],
            action='show',
            id='error-file-not-found'
        )
    elif key == 'PermissionError':
        return dmc.Notification(
            message="You do not have sufficient permission to access that file!",
            title="Warning",
            color='red',
            icon=[DashIconify(icon="ep:warning")],
            action='show',
            id='error-permissions'
        )
    elif key == 'FileRequiredError':
        return dmc.Notification(
            message="You must have an Open File in File Explorer to do this action!",
            title="Warning",
            color='red',
            icon=[DashIconify(icon="ep:warning")],
            action='show',
            id='error-permissions'
        )
    elif key == 'NameRequiredError':
        return dmc.Notification(
            message="A Render App Name is required to do this action!",
            title="Warning",
            color='red',
            icon=[DashIconify(icon="ep:warning")],
            action='show',
            id='error-permissions'
        )
    elif key == 'GitNotInstalledError':
        return dmc.Notification(
            message="Git must be installed on your system to deploy to Render.com!",
            title="Warning",
            color='red',
            icon=[DashIconify(icon="ep:warning")],
            action='show',
            id='error-permissions'
        )
    elif key == 'NotGitRepoError':
        return dmc.Notification(
            message="You must publish your project to Git before continuing!",
            title="Warning",
            color='red',
            icon=[DashIconify(icon="ep:warning")],
            action='show',
            id='error-permissions'
        )