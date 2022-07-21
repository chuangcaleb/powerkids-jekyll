---
layout: default
permalink: events/comm
title: Community Service
nav: events
---

{% include pk/masonry.html %}

<div class="container py-4 mb-2 col-xl-10">
	<div class="row row-cols-1 row-cols-lg-2">
		
		<div class="col text-center m-auto">
			<h1 class ="display-4 my-4">Community Service</h1>
			<p class="lead fs-3 my-4">
				{% include pk/powerkids.html %} supports the work of the
				<br>
				<a href="http://www.fungatessuperflowfoundation.org" target="_blank" rel="noopener noreferrer">
					FunGates Superflow Foundation</a>.
			</p>

			<p class="lead">
				A portion of your child's monthly school fees is channelled to support FunGates SuperFlow Foundation. You played part in the community work when you registered your child with PowerKids. Our staff get to serve in Love-On-Wheels and the Soup Kitchen.
			</p>

			<p class="lead">
				At {% include pk/powerkids.html %}, we teach <strong>CARE</strong> by serving. 
			</p>

			<p class="lead">
				The 6-years-olds' field trip to the Soup Kitchen is a rich experience for their young age.
			</p>
		</div>

		<div class="col">
			<img src="/assets/images/events/pspkidsfoundation_orig.jpg" class="w-auto mx-auto d-block" alt="...">
		</div>

	</div>

</div>

<div class="container-fluid container-md mb-4">

    <div class="row g-2" data-masonry="{&quot;percentPosition&quot;: true }" style="position: relative;">

        {% for imgpath in site.data.img_dir.comm %}

                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <img src="/assets/images/events/comm/{{ imgpath }}" alt="image"/>
                </div>

        {% endfor %}

    </div>

</div>