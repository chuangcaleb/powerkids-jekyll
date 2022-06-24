---
layout: default
permalink: programs/morning
---

<script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>

<div class="p-3">
    <div class="container py-3 col-xl-10">
        <div class="mb-5" id="morning-desc">
            <h2>Morning School&nbsp;
                <br class="d-sm-none"><small class="text-muted">8.30am to 12.30pm</small>
            </h2>
            <p class="lead">
                Early childhood education provided for children from age 2 to age 6. There will be emphasis on building social emotion to cognitive study from very young age.  PowerKids has a track record of strong academics and good character transformation.
            </p>
        </div>

        <div class="row g-2" data-masonry="{&quot;percentPosition&quot;: true }" style="position: relative; height: 690px;">
            {% for image in site.static_files %}
                {% if image.path contains 'images/programs/morn/' %}
                    <div class="col-sm-6 col-lg-4 col-xl-3">
						<img src="{{ site.baseurl }}{{ image.path }}" alt="image"/>
					</div>
                {% endif %}
            {% endfor %}
        </div>

    </div>
</div>