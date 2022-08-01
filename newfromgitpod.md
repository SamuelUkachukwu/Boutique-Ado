Bring your own workspace SSH keys
Published on July 18, 2022, see also https://www.gitpod.io/changelog

image

SSH (secure shell) is a critical protocol for remote development. Both JetBrains IDEs and the VS Code editor use SSH as their remote development foundation. So, a big focus at Gitpod has been on improving performance and usability for connecting using SSH.

Which is why today we're excited to announce that in Gitpod you can now upload your own public keys to access your workspace. In addition, we've also removed the requirement for a mandatory public key to be available when access Gitpod using SSH with an Access Token. With SSH public key upload you can now:

Re-connect to workspaces without needing to go back to the Gitpod dashboard.
Benefit from improved security when accessing your workspace with a private key.
See the announcement post for details on the use-cases, benefits and how to get started using your own key pair with Gitpod today.

Contributors: iqqbot, mustard-mh

Roadmap updates
JetBrains - Roadmap issue: #7956 beta

#11209 - Add support for JetBrains Gateway v222.3345.1 and later. Contributors: akosyakov, felladrin, loujaybee
#11307 - Gitpod Plugin for JetBrains IDEs was updated to respect network proxies. Contributors: akosyakov, felladrin
Fixes and improvements
Gitpod Core
#11409 - Improve Git Integration validation by testing if host is reachable. Contributors: AlexTugarev, MrSimonEmms, geropl, jldec
#11400 - Switch to http/1.1 for gitlab.com repositories Contributors: aledbf, jenting, kylos101
#11341 - [local-preview] show DOMAIN in the output Contributors: Pothulapati, adrienthebo
#11237 - [kots]: add node CPU/memory check tests to workspace node only Contributors: MrSimonEmms, lucasvaltl, nandajavarma
#11253 - Requests on ws-proxy won't contain the port anymore on the "X-Forwarded-Host" header. It will contain only the host. If you need the port, you can get it from the "X-Forwarded-Port" header. Contributors: aledbf, felladrin
#11208 - Users can see their billable sessions. Contributors: andrew-farries, laushinka
#11205 - Minor fixes to the old Team Subscription UI Contributors: andrew-farries, geropl
#11192 - Make prebuild logs responsive for small viewports Contributors: andrew-farries, geropl, gtsiolis, laushinka
#11232 - Fix an issue that was causing the workspace to frequently timeout when using a JetBrains IDE. Contributors: akosyakov, felladrin, mustard-mh
#11268 - [installer]: add test for customization of proxy service Contributors: MrSimonEmms, nandajavarma
Gitpod VSCode Browser
#379 - Fix .gitpod.yml ports.onOpen not working on workspace startup Contributors: jeanp413, mustard-mh
#378 - Remove heartbeat in gitpod-remote VS Code plugin Contributors: jeanp413
Gitpod VSCode Desktop
#6 - Fix auth validation Contributors: jeanp413
#5 - Use new getSSHPublicKeys api method Contributors: jeanp413