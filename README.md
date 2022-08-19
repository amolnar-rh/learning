# netlify

This script is used to automate your request for a netlify build based on the following command:

`curl -H 'Content-Type: application/json' --request POST --data '{"PR_BRANCH":"BRANCH_NAME","BASE_REPO":"openshift/openshift-docs","PR_NUMBER":"PR_NUMBER","USER_NAME":"GITHUB_USERNAME","BASE_REF":"main","REPO_NAME":"GITHUB_USERNAME/openshift-docs"}' https://eoa6vg2jiwjbnh6.m.pipedream.net`

The script makes use of the GitHub CLI to automatically populate the variables that you would have to otherwise manually type in every time.


*NOTE: This solution assumes that you have one PR open per working branch. If you have multiple PRs open for the same branch, the script will stop and exit with an error message.*

Prerequisites
* [You installed GitHub CLI](https://cli.github.com/manual/)

Procedure
1. Download the script with `wget https://raw.githubusercontent.com/amolnar-rh/learning/netlify/netlify -O ~/Downloads/netlify`
2. Move the file to your `bin` directory with `sudo mv ~/Downloads/netlify /usr/local/bin/netlify` 
3. Make the file executable with `chmod +x /usr/local/bin/netlify`
4. Use the script from your local openshift-docs repository by typing `netlify`.
