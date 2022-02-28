# Point to point VPN
This directory is intended to help set up a point to point (AKA peer to peer) VPN
to assist with remote mentoring. The basic idea is that an overlay network is established
between the local machine and the remote machine.

To set up the networking, you need to do the following steps:
1. Edit `./install` to set the local and remote addresses and the publicly reachable
IP address for the remote machine. That address must accept UDP on port 51280. 
1. Run `sh ./install` to generate the configuration and launch files and crypto keys
2. Paste the public key displayed in step 1 (and stored in `public`) into the other machines configuration file.
3. Run `sh ./start` to launch the local side of the VPN
4. Run the comparable command on the other side
5. Both machines will be able to communicate with addresses specified in `install`