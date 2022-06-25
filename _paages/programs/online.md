---
layout: default
permalink: programs/online
title: Online School
---

<script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>

<div class="container py-4 mb-2 col-xl-10">
    <div class="row row-cols-1 row-cols-md-2 g-4">

        <div class="col px-md-4" id="morning-desc">
            <h2 class="row row-cols-auto align-items-end mb-4 gx-4">
                <div class="col">
                    <span class="display-5">
                        Online School
                    </span>
                </div>
                <div class="col my-auto">
                    <small class="text-muted">
                        Schooling hours
                    </small>
                </div>
            </h2>
            <p class="lead">
                Our teachers are engaging on-screen, providing First Class Fun Learning even if you are unable to come to our physical school.
            </p>
        </div>

        <div class="col order-md-first d-flex align-items-center">
            <div class="video-embed ratio ratio-16x9">
                <iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen frameborder="0" src="https://www.youtube.com/embed/H2vVU91AmAQ"></iframe>
            </div>
        </div>

    </div>


</div>

<div class="container-fluid container-md mb-4">
    <div class="row g-2" data-masonry="{&quot;percentPosition&quot;: true }" style="position: relative; height: 690px;">
        {% for image in site.static_files %}
            {% if image.path contains 'images/programs/online/' %}
                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <img src="{{ site.baseurl }}{{ image.path }}" alt="image"/>
                </div>
            {% endif %}
        {% endfor %}
    </div>
</div>