---
layout: default
nav: programs
---

{% assign programs_dir = "/assets/images/programs" | relative_url %}

<div class="p-4">
    <div class="container py-3 col-xxl-10">

        <h1 class="display-4 fw-bold text-center mb-4 mb-md-5">Programs</h1>

        <div class="row row-cols-1 row-cols-xl-2 g-3">

			{% include pk/pg/morning-card.html %}
			{% include pk/pg/after-card.html %}
			{% include pk/pg/daycare-card.html %}
			
        </div>

    </div>
</div>