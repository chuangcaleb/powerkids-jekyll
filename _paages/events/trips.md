---
layout: default
permalink: events/trips
title: Field Trips
nav: events
---

<div class="container py-4 mb-2 col-xl-10 text-center">
	
	<h1 class="display-4 my-lg-4">Field Trips</h1>
	
	<p class="lead fs-5 mx-auto">
		Field trips help bring learning outside the classroom, giving children a new perspective and boost cognitive development. 
	</p>
	<p class="lead fs-5 mx-auto">
	These trips offer diverse learning opportunities, improve health and allow children to get authentic experiences.
	</p>

	<div class="my-5">

		<div class="row g-2" data-masonry="{&quot;percentPosition&quot;: true }" style="position: relative;">
	
			{% for imgpath in site.data.img_dir.trips %}
	
					<div class="col-sm-6 col-lg-4 col-xl-3">
						<img src="/assets/images/events/trips/{{ imgpath }}" alt="image"/>
					</div>
	
			{% endfor %}
		   
		</div>
	
	</div>

	<h5 class="">Other places we have visited:</h5>
	<p class="fs-5">Bomba • Aquaria • Hair Saloon • EcoFarm • Bank Negara • National Science Centre • Grocery Shopping • Zoo Negara • Kidzania</p>

</div>

