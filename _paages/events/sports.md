---
layout: default
permalink: events/sports
title: Sports Day
nav: events
---

{% include pk/masonry.html %}

<div class="container py-4 mb-2 col-xl-10">
	<div class="row row-cols-1 row-cols-md-2">
		<div class="col my-auto">
			<div class="col-md-10 text-center mx-auto">
				<h1 class ="display-5">Sports Day</h1>
				<p class="lead">It's about championship, sportsmanship, winning, competing, participation, and most of all: a family day out. A wonderful sight of parent-children games.</p>
			</div>
		</div>
		<div class="col order-md-first">
			<div class="video-embed ratio ratio-16x9">
				<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen frameborder="0" src="https://www.youtube.com/embed/vj-9e65wtPE"></iframe>
			</div>
		</div>
	</div>

</div>

<div class="container-fluid container-md mb-4">

    <div class="row g-2" data-masonry="{&quot;percentPosition&quot;: true }" style="position: relative;">

        {% for imgpath in site.data.img_dir.sports %}

                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <img src="/assets/images/events/sports/{{ imgpath }}" alt="image"/>
                </div>

        {% endfor %}
       
    </div>

</div>