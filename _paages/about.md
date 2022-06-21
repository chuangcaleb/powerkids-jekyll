---
layout: default
---

<!-- <h1 class="display-3 text-center p-4 mb-0 text-bg-dark">About</h1> -->

{% assign about_dir = "/assets/images/about" | relative_url %}

<div class="p-4 mb-4 rounded-3 bg-light">
    <div class="container-fluid py-3 col-md-7">
        <h1 class="display-3 text-center mb-4">About</h1>
        <div class="mb-4">
            <p class="lead">
                {% include pk/powerkids.html %}
                was founded in 2001, based on the Fungates curriculum. We empower your little child’s early education by injecting play and care to stimulate your little one’s learning.
            </p>
            <p class="lead">
                Guided by educational policies from Ministry of Education Malaysia and Jabatan Kebajikan Malaysia, we constantly keep up with best practices to ensure our students become competent learners to navigate the 21st-Century world.
            </p>
            <p class="lead">
                {% include pk/powerkids.html %}... Opening the Gates to First-Class Fun Learning!
            </p>
        </div>
    </div>
</div>

<div class="container px-3 py-3 col-md-7" id="icon-grid">
    <div class="container-md row row-cols-1 row-cols-sm-2 g-4 py-4 mx-0">
        <div class="col d-flex align-items-start">
            <i class="bi-award text-muted flex-shrink-0 me-3 display-6"></i>
            <div>
                <h4 class="fw-bold mb-0">Fungates Programme</h4>
                <p>Positive reinforcement of 21st century learning.</p>
            </div>
        </div>
        <div class="col d-flex align-items-start">
            <i class="bi-balloon-heart text-muted flex-shrink-0 me-3 display-6"></i>
            <!-- <i class="bi-emoji-laughing text-muted flex-shrink-0 me-3 display-6"></i> -->
            <div>
                <h4 class="fw-bold mb-0">Emotional Well-Being</h4>
                <p>Caring beyond academics.</p>
            </div>
        </div>
        <div class="col d-flex align-items-start">
            <i class="bi-mortarboard text-muted flex-shrink-0 me-3 display-6"></i>
            <div>
                <h4 class="fw-bold mb-0">Trained, Qualified Teachers</h4>
                <p>Our teacher's skills are upgraded constantly.</p>
            </div>
        </div>
        <div class="col d-flex align-items-start">
            <i class="bi-binoculars text-muted flex-shrink-0 me-3 display-6"></i>
            <div>
                <h4 class="fw-bold mb-0">Apparatus</h4>
                <p>Equipped with a variety of tools to inspire learning.</p>
            </div>
        </div>
        <div class="col d-flex align-items-start">
            <i class="bi-pc-display-horizontal text-muted flex-shrink-0 me-3 display-6"></i>
            <div>
                <h4 class="fw-bold mb-0">Technology</h4>
                <p>Tech is integrated into learning and teaching environment.</p>
            </div>
        </div>
        <div class="col d-flex align-items-start">
            <i class="bi-cloud-sun text-muted flex-shrink-0 me-3 display-6"></i>
            <div>
                <h4 class="fw-bold mb-0">Environment</h4>
                <p>Clean, spacious environment for for cheerful children.</p>
            </div>
        </div>
        <div class="col d-flex align-items-start">
            <i class="bi-house-heart text-muted flex-shrink-0 me-3 display-6"></i>
            <div>
                <h4 class="fw-bold mb-0">Premises</h4>
                <p>Child-centric design to encourage socialisation and play learning.</p>
            </div>
        </div>
    </div>
</div>

<div class="row justify-content-md-center py-5 bg-dark mx-0">
    <div class="col-md-10 row mx-0">

        <div class="col-10 col-sm-8 col-lg-6 mx-auto my-3">
            <img src="{{about_dir}}/apple-girl.jpg" class="d-block w-100 " alt="...">
        </div>
        <div class="col-md mx-auto"></div>
        <div class="col-lg-5 d-flex align-items-center flex-column my-auto">
            <div class="text-center text-white mb-3">
                <h2 class="display-3 fw-bold lh-1 my-4">Our Vision</h2>
                <p class="lead fs-3">To raise a new generation of 21st-Century Children with
                    <span class="underline">heart</span>.</p>
            </div>
            <button class="btn btn-primary btn-lg px-4 me-md-2" type="button">Our Community Service</button>
        </div>
    </div>
</div>

<div class="row justify-content-md-center py-5 mx-0">
    <div class="col-md-10 row align-items-between mx-0">
        <div class="col-lg-6 d-flex flex-column my-auto">
            <div class="d-flex align-items-center flex-column mb-3">
                <h2 class="display-3 fw-bold lh-1 my-4">Our Mission</h2>
                <div class="lead fs-3">
                    <p>
                        <span class="display-4" style="color:red">A</span>cademic Excellence</p>
                    <p>
                        <span class="display-4" style="color:blue">B</span>uilding Character</p>
                    <p>
                        <span class="display-4" style="color:darkgoldenrod">C</span>ultivating Moral & Spiritual Values</p>
                </div>
            </div>
        </div>
        <div class="col-md mx-auto"></div>
        <div class="col-10 col-sm-8 col-lg-4 mx-auto my-3">
            <img src="{{about_dir}}/21yrs.jpeg" class="d-block w-100" alt="..." style="transform:rotate(10deg)">
        </div>
        <!-- <div class="col-md mx-auto"></div> -->
    </div>
</div>

<div class="p-4 bg-primary text-bg-primary text-center">
    <div class="container-fluid py-md-3 col-md-9 g-0">
        <h2 class="display-3 fw-bold lh-1 my-4">Our Team</h2>
        <p class="lead">At PowerKids, we have trained, qualified teachers who are passionate and dynamic. Their joy comes from seeing our little learners light up as they make new friends or learn new letters, words or concepts.
        </p>
        <p class="lead">Every class teacher is qualified in Early Childhood Education and further up-graded with latest FunGates teaching practices on yearly basis. Our teaching team is up-to-date on trainings by KSPK Ministry of Education of Malaysia for guru-guru pra-sekolah.</p>
        <br>
        <p class="lead">“Children’s First” is our basis to all our decisions in managing children entrusted to our care.</p>
    </div>
</div>

<div class="pt-5 p-md-5 bg-dark text-center">

    <div class="card col-md-10 mx-auto">
        <h2 class="card-header display-6 fw-bold lh-1 py-4">Sri Petaling</h2>
        <div class="card-body">
            <div class="col-md-11 row row-cols-1 row-cols-md-2 g-4 mx-auto">
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

    <div class="col-md-10 row row-cols-1 row-cols-md-2 pt-5 g-0 gy-5 g-md-3 mx-auto">

        <div class="col">
            <div class="card shadow-sm">
                <h2 class="card-header display-6 fw-bold lh-1 py-4">Salak South Garden</h2>
                <img src="{{about_dir}}/k45.jpeg" class="card-img-top" alt="...">
            </div>
        </div>

        <div class="col">
            <div class="card shadow-sm">
                <h2 class="card-header display-6 fw-bold lh-1 py-4">Bukit Jalil</h2>
                <img src="{{about_dir}}/jalil.jpg" class="card-img-top" alt="...">
            </div>
        </div>

        <div class="col">
            <div class="card shadow-sm">
                <h2 class="card-header display-6 fw-bold lh-1 py-4">Puchong BK9</h2>
                <img src="{{about_dir}}/puchong.jpg" class="card-img-top" alt="...">
            </div>
        </div>

        <div class="col">
            <div class="card shadow-sm">
                <h2 class="card-header display-6 fw-bold lh-1 py-4">Parklane OUG</h2>
                <img src="{{about_dir}}/parklane.jpg" class="card-img-top" alt="...">
            </div>
        </div>

    </div>

</div>
