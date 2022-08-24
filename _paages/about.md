---
layout: default
nav: about
---

{% assign about_dir = "/assets/images/about" | relative_url %}

<div class="p-4 bg-light">
    <div class="container py-3 col-md-9 col-xl-7">
        <h1 class="display-4 fw-bold text-center mb-4">About</h1>
        <div class="mb-4 lead">
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
    </div>
</div>

{% include pk/mv.html %}

<div class="our-team p-4 bg-primary text-bg-primary text-center">
    <div class="container-fluid py-md-3 col-md-10 g-0 mb-4">
        <h2 class="display-3 fw-bold lh-1 my-4">Our Team</h2>
        <div class="our-team-body lead">
            <p>At PowerKids, we have trained, qualified teachers who are passionate and dynamic. Their joy comes from seeing our little learners light up as they make new friends or learn new letters, words or concepts.
            </p>
            <p>Every class teacher is qualified in Early Childhood Education and further up-graded with latest FunGates teaching practices on yearly basis. Our teaching team is up-to-date on trainings by KSPK Ministry of Education of Malaysia for guru-guru pra-sekolah.</p>
            <br>
            <p>“Children’s First” is our basis to all our decisions in managing children entrusted to our care.</p>
        </div>
    </div>
</div>

<div class="our-team-divider"></div>

<div class="school-teams bg-dark text-center pb-4">

    <div class="container py-4">

        <div class="card mx-xl-5">
            <h2 class="card-header display-6 fw-bold lh-1 py-3">Sri Petaling</h2>
            <div class="body-card py-2 py-lg-4">
                <div class="row row-cols-1 row-cols-md-2 g-3 g-lg-4 mx-auto">
                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{{about_dir}}/s2-age-4.jpeg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Age 4 Teachers</h5>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{{about_dir}}/s2-age-5.jpeg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Age 5 Teachers</h5>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{{about_dir}}/s2-age-6.jpeg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Age 6 Teachers</h5>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card shadow-sm">
                            <img src="{{about_dir}}/s2-admin.jpeg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">Administration Team</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row row-cols-1 row-cols-md-2 g-0 gy-3 g-lg-4 my-0 mx-xl-4">

            <div class="col">
                <div class="card shadow-sm">
                    <h2 class="card-header fs-2 fw-bold lh-1 py-3">Salak South Garden</h2>
                    <img src="{{about_dir}}/k45.jpeg" class="card-img-top" alt="...">
                </div>
            </div>

            <div class="col">
                <div class="card shadow-sm">
                    <h2 class="card-header fs-2 fw-bold lh-1 py-3">Bukit Jalil</h2>
                    <img src="{{about_dir}}/jalil.jpeg" class="card-img-top" alt="...">
                </div>
            </div>

            <div class="col">
                <div class="card shadow-sm">
                    <h2 class="card-header fs-2 fw-bold lh-1 py-3">Puchong Utama</h2>
                    <img src="{{about_dir}}/puchong.jpg" class="card-img-top" alt="...">
                </div>
            </div>

            <div class="col">
                <div class="card shadow-sm">
                    <h2 class="card-header fs-2 fw-bold lh-1 py-3">Parklane OUG</h2>
                    <img src="{{about_dir}}/parklane.jpg" class="card-img-top" alt="...">
                </div>
            </div>

        </div>

    </div>

    <a class="text-decoration-none my-lg-5 d-inline-flex align-self-center" href="/schools">
        <button class="btn btn-outline-light btn-lg">Our Five Schools →</button>
    </a>

</div>

{% include pk/embed-reel.html %}

{% include pk/bottom-action.html %}
