---
layout: default
nav: events
---

{% assign events_dir = "/assets/images/events" | relative_url %}

<div class="p-4">
    <div class="container-md py-3 col-xxl-10">

        <h1 class="display-4 fw-bold text-center mb-4 mb-md-5">Events</h1>

        <div class="row row-cols-1 row-cols-sm-2 g-2 g-md-5">

            <div class="graduation col px-xl-5">
                <div class="card hover-fade hover-shadow h-100">

					<div class="">
						<img src="{{events_dir}}/graduation.jpg" class="w-auto mx-auto d-block" alt="...">
                    </div>
					
					<div class="card-body h-100 d-flex justify-content-center">
						<h2 class="card-title align-self-center">Graduation</h2>
					</div>

					<a class="stretched-link" href="/events/grad"></a>

                </div>
            </div>

            <div class="sports col px-xl-5">
                <div class="card hover-fade hover-shadow h-100">

                    <div class="">
                        <img src="{{events_dir}}/Event_sports3_resized.JPG" class="w-auto mx-auto d-block" alt="...">
                    </div>

                    <div class="col-sm">
                        <div class="card-body h-100 d-flex justify-content-center">
                            <h2 class="card-title align-self-center">Sports Day</h2>
                        </div>
                    </div>

					<a class="stretched-link" href="/events/sports"></a>
					
                </div>
            </div>

            <div class="trips col px-xl-5">
                <div class="card hover-fade hover-shadow h-100">

                    <div class="">
                        <img src="{{events_dir}}/DSCF0241.JPG" class="w-auto mx-auto d-block" alt="...">
                    </div>

                    <div class="col-sm">
                        <div class="card-body">
                            <h2 class="card-title text-center">Field Trips</h2>
                            <a class="stretched-link" href="/events/trips"></a>
                        </div>
                    </div>

                </div>
            </div>

            <div class="comm col px-xl-5">
                <div class="card hover-fade hover-shadow h-100">

                    <div class="">
                        <img src="{{events_dir}}/Event_FSF2.JPG" class="w-auto mx-auto d-block" alt="...">
                    </div>

                    <div class="col-sm">
                        <div class="card-body">
                            <h2 class="card-title text-center">Community Service</h2>
                            <a class="stretched-link" href="/events/comm"></a>
                        </div>
                    </div>

                </div>
            </div>

        </div>

    </div>
</div>