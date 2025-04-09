# Linux Patch Management: How to Patch Linux OS Vulnerabilities

## Overview

This document outlines the process of Linux patch management, particularly focusing on Red Hat-based systems. It includes steps to identify outdated packages, update them, and verify the patching process.

---

## 🔧 Prerequisites

- Root user privileges
- Internet connectivity (for fetching updates)
- Recommended: Snapshot/backup before patching

---

## 🧪 Step 1: Identify Installed Packages

```bash
# List all installed packages using RPM
rpm -qa

# OR using YUM
yum list installed
```

---

## 🗂 Step 2: Check OS Version and Repositories

```bash
# Check OS version
cat /etc/os-release

# List available repositories
ls /etc/yum.repos.d/
```

---

## 🔍 Step 3: Check for Available Updates

```bash
# Show packages available for update
yum check-update

# Optional: List repositories in use
yum repolist
```

> **Note**: Always perform patch testing on SIT/UAT environments before applying to production.

---

## ⬆️ Step 4: Apply Updates

```bash
# Run update (will show versions before upgrading)
yum update
```

- Reviews and fetches new packages
- Installs security and kernel updates
- Handles cleanup of unused packages

---

## 🔁 Step 5: Reboot After Patching

```bash
# Reboot to apply kernel and system changes
reboot
```

> Reboot is essential to load updated kernels and apply system-level patches.

---

## ✅ Step 6: Verify Patch Status

After reboot:

```bash
# Check for any remaining updates
yum check-update
```

- If nothing is listed, the system is up-to-date.
- Optionally, generate a report for audit purposes.

---

## 🧾 Optional: Reporting for Compliance

- Save `yum update` logs
- Share updated package list with security/governance teams
- Use for audit trails

---

## 🔚 Conclusion

Patch management is essential to maintain Linux system security and stability. Always test before production deployment, take backups, and verify patch success post-reboot.

> Happy Learning! For more content, like, share, and subscribe to the channel.
