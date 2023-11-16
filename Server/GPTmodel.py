def giveResults():
    result = {
        "Software": software_list[0]+"\n"+software_list[1],
        "Hardware": "This is the result from the GPT model for the hardware requirement",
        "Network": "This is the result from the GPT model for the network requirement",
        "Security": "This is the result from the GPT model for the security requirement",
    }
    return result

res_for_software = """The main software requirements from the texts in detail are:
- Application & IT security is an essential requirement from the JCB perspective, and the Solution Provider must make sure that the developed system is robust and secure.
- Solution Provider shall make sure that while designing and developing the system all software, data security measures are considered, and platform developed is robust and secure.
- Solution Provider facility should have necessary security certifications to protect confidential information and data.
- Solution Provider shall have the policy for regular security assessment of the Application and subsequently their closure.
- Internal prevention and monitoring systems such as Firewalls, Anti-Virus, Endpoint control, internet, and email filtering must be implemented in the Solution Provider’s facility.
- DR (Disaster Recovery) failover Architecture is necessary.
- Identity Management - Needs unique and strong identification of devices; Timely renewal/update of device status to enforce required credential checks.
- Ensure mutual authentication; data in motion confidentiality; secure connections.
- Access to APIs, executables, etc. should be access controlled; Ability to allocate or revoke access at any time.
- Protection of data at rest, data in use and data in transit must be provided; Capability to purge any data at will is needed.
- All-access to the software layer should be access controlled. Authorization levels will determine how the software layer is used.
- Confidentiality and integrity shall be provided for identity credentials.
- Individual layers must be isolated from other processes. The Internet-facing layer must be isolated from other layers.
- Integrity and authenticity of updates must be ensured; all such updates must be traceable and logged; prior approval must be enforced before any update.
- An application must be accessible only via secure communication ensuring authenticity, integrity, and confidentiality.
- Access rights must be implemented, and it should be possible to grant, review or revoke at will. Role-based authorization is needed to limit access to data.
- Secure session management must be followed covering but not limited to ID properties (name, length, content, etc.) and ID lifecycle (generate, verify, renew, and invalidate).
- Ensure protection against cross-site scripting and injection. Most importantly, all data must be validated, and query parameterization and data encoding be implemented.
- DOS (Denial of Service) Protection
- Application logging is needed. It must track critical application-level changes (examples: CMH refresh, user credential update, etc.) The integrity of an audit log is a must.
- Users must be managed uniquely. Create, Read, Update and Delete must be enabled and made available based on roles.
- Firmware/Code coverage shall be 100%. 100% code coverage means having 100% of the code with unit tests.
- Firmware development life cycle (FDLC) shall follow development process template which shall cover key areas like development methodology, process followed, traceability, requirement, version control etc.
- SRS (software requirement specification) shall cover all types of embedded stack used and its license details and validity.
- Each firmware release shall consist of version control, feature matrix, SRS, impact analysis, code coverage with results, test reports, development/change request document, root cause analysis in case of bug fix, negative test case report, and code & test quality report.
- Firmware shall support CAN SAE J1939 protocol and UDS protocol.
- LiveLink Firmware shall support protocols such as TCP/IP - MQTT, HTTP(s), FTP, RS232 UART, Bluetooth, Wi-Fi, and USB.
- If both in-machine and remote device configuration is not set, then default configurations shall be in place.
- In case remote configuration or in-machine configuration fails, then device shall retain previous configuration or shall be able to reset to default configurations.
- In case of device firmware is in hang-up or unknown state, Emergency recovery firmware module shall act as a recovery agent.
- Device firmware shall support In-machine configuration through CAN J1939 or Bluetooth.
- Configuration manager application running on PC, Smart device or server shall have same user interface and experience.
"""
software_summary = """
    1. Data preprocessing
    2. Feature engineering
    3. Hyperparameter tuning
    4. Ensemble methods
    5. Transfer learning
    6. Data augmentation
    7. Regularization
    8. Data bias
    9. Error analysis"""

software_list = []
software_list.append(res_for_software)
software_list.append(software_summary)