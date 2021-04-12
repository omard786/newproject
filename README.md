# newproject
this is my 2nd project with qa

<h1>About the project:</h1>

<p>getting started(requirments.txt)</p>

<h1> Requirements</h1>

<p> An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project. This could also provide a record of any issues or risks that you faced creating your project.

An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
The project must follow the Service-oriented architecture that has been asked for.

The project must be deployed using containerisation and an orchestration tool.

As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
The project must make use of a reverse proxy to make your application accessible to the user. </p>

<h2>roadmap: There will be a total of 4 micro-services:</h2>

<p><b>service 1</b>
 this would be my random number generator the goal of this is to have 8 numbers generated randomly (1-8) 4 even and 4 odd numbers.

<b>service 2</b>
this would be my random letter generator with 4 vowels (A,E,I,U) and 4 non-vowels (B,F,J,V)

<b>service 3</b>
 this would bring the mixed string (8 random letter and numbers (4 of each)) together and then have the string pinned against a set criteria in order to win a prize. the conditions would be as follows: 2 even + 2 vowels = gold prize 2 even + 1 vowel / 1 even + 2 vowels = silver prize 2 even or 2 vowels = bronze prize 1 even or 1 vowel = no prize ("you lose")

<b>service 4 </b>
 this would be the front end i.e flask + html</p>

<h1>continous intergration:</h1>
 in order to present this i would need to have alternative string outputs for my variable genarators, this would be shown by combining s2 and s3 together in s4 and communicating that to service 1 (front-end). to show it will accept and intergrate new code another variation of the generator would be developed on another branch to show off this change. 


 <h1> Risk Assessment </h1>

 <img src="img/risk.png">

 