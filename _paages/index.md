---
layout: default
title: Home
nav: home
---

{% include pk/home-carousel.html %}
{% assign about_dir = "/assets/images/about" | relative_url %}
{% assign schools_dir = "/assets/images/schools" | relative_url %}

<div class="container-md p-md-4">
    <div class="container-fluid col-lg-10 col-xl-9 col-xxl-8 py-4">

        <h1 class="display-3 fw-bold mb-4">
            Welcome to
            {% include pk/powerkids.html %}!
        </h1>

        <div class="jumbo-body mb-4 lead">
            <p>
                {% include pk/powerkids.html %}
                was founded in 2001, based on the Fungates curriculum. We empower your little child’s early education by injecting play and care to stimulate your little one’s learning.
            </p>
            <p>
                Guided by educational policies from Ministry of Education Malaysia and Jabatan Kebajikan Malaysia, we constantly keep up with best practices to ensure our students become competent learners to navigate the 21st-Century world.
            </p>
            <p>
                {% include pk/powerkids.html %}... Opening the Gates to First-Class Fun Learning!
            </p>
        </div>

        <a href="/about">
            <button class="btn btn-primary btn-lg px-4">Learn More</button>
        </a>

    </div>

</div>

{% include pk/embed-reel.html %}

{% include pk/mv.html %}

<div class="container-fluid text-bg-dark">

    <div class="p-3 p-md-4 d-flex justify-content-lg-center">
        <h1 class="display-4 fw-bold mb-0">
            Our Five Schools
        </h1>
        <a class="text-decoration-none ms-lg-5 d-inline-flex align-self-center" href="/schools">
            <button class="btn btn-outline-light btn-lg">Learn More →</button>
        </a>
    </div>


    <div class="row row-cols-1 row-cols-md-5 text-center" id="school-list">
        <div class="col bg-red py-3">
            <h2 class="fs-1 mb-3">Sri Petaling</h2>
            <div class="school-picture d-flex align-items-stretch">
                <img src="{{schools_dir}}/sri-petaling.jpeg" class="d-block h-100 my-auto" alt="...">
            </div>
        </div>
        <div class="col bg-blue py-3">
            <h2 class="fs-1 mb-3">Salak South Garden</h2>
            <div class="school-picture d-flex align-items-stretch">
                <img src="{{schools_dir}}/k45-edited-wires.jpeg" class="d-block h-100 my-auto" alt="...">
            </div>
        </div>
        <div class="col bg-red py-3">
            <h2 class="fs-1 mb-3">Bukit Jalil</h2>
            <div class="school-picture d-flex align-items-stretch">
                <img src="{{schools_dir}}/jalil.jpeg" class="d-block h-100 my-auto" alt="...">
            </div>
        </div>
        <div class="col bg-blue py-3">
            <h2 class="fs-1 mb-3">Puchong Utama</h2>
            <div class="school-picture d-flex align-items-stretch">
                <img src="{{schools_dir}}/puchong.jpg" class="d-block h-100 my-auto" alt="...">
            </div>
        </div>
        <div class="col bg-red py-3">
            <h2 class="fs-1 mb-3">Parklane OUG</h2>
            <div class="school-picture d-flex align-items-stretch">
                <img src="{{schools_dir}}/parklane.jpg" class="d-block h-100 my-auto" alt="...">
            </div>
        </div>
    </div>
</div>

{% include pk/bottom-action.html %}
