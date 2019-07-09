WebLogic on Docker
===============
This is a sample Docker configuration to setup and start a weblogic on development mode with a set of applications / libraries pre-deployed.

To create Data Sources, JMS Servers and deploy applications we use WLST. 

You cand find a full command reference at https://docs.oracle.com/cd/E24329_01/web.1211/e24490/quick_ref.htm.

To customize you have to update <code>deploy.py</code> file with your instructions.

To build:

<code>docker build -t wls .</code>

To run:

<code>docker run --name wls -d --rm -p 7001:7001 -p 9002:9002 wls</code>

You can access the AdminServer Web Console at https://localhost:9002/console.
