---
layout: default
permalink: programs/after
title: After School Program
nav: programs
---

{% assign after_dir = "/assets/images/programs/after" | relative_url %}


<div class="container py-4 mb-2 col-xl-10">
    <div id="after-desc" class="pb-4 mb-3">
        <h2 class="row row-cols-auto align-items-end mb-4 gx-4">
            <div class="col">
                <span class="display-5">
                    After School Program
                </span>
            </div>
            <div class="col my-auto">
                <small class="text-muted">
                    12:30am to 3:00pm
                </small>
            </div>
        </h2>
        <p class="lead">
            Learning is beyond academics. Lunch and homework coaching in the beginning part of the program daily.  Enrichment classes like Domestic Science to explore kitchen skills, Creative Art and Craft sessions, Speech & Drama into the world of imagination and stepping out to speak with confidence, Information Technology Communication to learn on latest gadgets is to keep up with time.
        </p>
    </div>

    <div class="row row-cols-1 row-cols-md-2 g-4">
        <div class="col">
            <img src="{{after_dir}}/ASP front with bleed.jpg" class="" alt="...">
        </div>
        <div class="col">
            <img src="{{after_dir}}/ASP back with bleed.jpg" class="" alt="...">
        </div>
        <div class="col">
            <img src="{{after_dir}}/ASP front with bleed chinese.jpg" class="" alt="...">
        </div>
        <div class="col">
            <img src="{{after_dir}}/ASP back with bleed chinese.jpg" class="" alt="...">
        </div>
    </div>

</div>


<div class="container-md my-5">
    <h2 class="display-6 mb-3">Check out our other Programs...</h2>
    <div class="row row-cols-1 row-cols-xl-2 g-3">

        {% assign programs_dir = "/assets/images/programs" | relative_url %}
        {% include pk/pg/morning-card.html %}
        {% include pk/pg/daycare-card.html %}

    </div>
</div>