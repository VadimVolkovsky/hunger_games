from random_user_agent.params import OperatingSystem, SoftwareName
from random_user_agent.user_agent import UserAgent

software_names = [SoftwareName.CHROME.value]
operating_systems = [
    OperatingSystem.WINDOWS.value,
    OperatingSystem.LINUX.value
]
user_agent_rotator = UserAgent(
    software_names=software_names,
    operating_systems=operating_systems,
    limit=100
)
