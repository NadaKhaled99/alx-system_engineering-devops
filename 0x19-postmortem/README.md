# README.md
# Requirements:

# Issue Summary (that is often what executives will read) must contain:
# 1-duration of the outage with start and end times (including timezone)
The outage lasted for 3 hours from 10:00 AM to 1:00 PM (UTC).
# 2-what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
The outage affected the email service, resulting in slow or failed delivery for approximately 30% of users.
# 3-what was the root cause
 The root cause was identified as a misconfiguration in the email server's routing settings.


# Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
# 1-when was the issue detected
Issue Detected: 10:00 AM (UTC)
# 2-how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
Detection Method: An engineer noticed a spike in error logs related to email delivery.
# 3-actions taken (what partsof the system were investigated, what were the assumption on the root cause of the issue)
Actions Taken: Investigated email server logs and network configurations. Initially assumed network congestion as the root cause.
# 6- misleading investigation/debugging paths that were taken
Misleading Paths: Investigated network hardware and potential DDoS attacks, leading to wasted time and resources.
# 4-which team/individuals was the incident escalated to
Escalation: Incident was escalated to the senior infrastructure team at 11:00 AM (UTC).
# 5-how the incident was resolved
Resolution: Identified the misconfiguration in the email server's routing settings and applied the necessary corrections by 1:00 PM (UTC).


# Root cause and resolution must contain:
# 1-explain in detail what was causing the issue
Cause: The issue stemmed from a misconfiguration in the email server's routing settings, causing emails to be rerouted incorrectly.
# 2-explain in detail how the issue was fixed
Resolution: Corrected the misconfiguration by updating the routing settings in the email server configuration files.

# Corrective and preventative measures must contain:
# 1-what are the things that can be improved/fixed (broadly speaking)
Improvements: Strengthen monitoring and alerting systems to detect similar misconfigurations promptly. Enhance documentation on server configurations to avoid future errors.
# 2-a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
1.Implement automated configuration checks for email server settings.
2.Conduct a thorough review of all server configurations for potential misconfigurations.
3.Enhance internal training programs to increase awareness of proper server configuration practices.
4.Develop a comprehensive incident response plan for faster resolution of similar issues in the future.

# Be brief and straight to the point, between 400 to 600 words

# While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

# Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
