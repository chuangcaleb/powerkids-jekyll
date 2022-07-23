---
layout: default
nav: register
---

<div class="container-fluid my-4 my-xl-5">
    <div class="col-xl-10 mx-auto row row-cols-1 row-cols-lg-2 g-4">

        <div class="col p-md-5 d-flex align-items-center">
            <div class="register-body mx-auto">

                <h1 class="display-4 fw-bold">Register with us!</h1>

                <ol class="register-steps lead ms-0 m-4">
                    <li>Complete and sign the Registration Form</li>
                    <li>Attach with photocopy of birth certificate​</li>
                    <li>Make full payment for registration</li>
                </ol>

                <a class="mx-auto" href="https://docs.google.com/forms/d/e/1FAIpQLScx6CBPRCpy701cuUepOTB2r7_d0DdaYDuIRtPN5U5OtV7phQ/viewform?usp=sf_link" rel="noopener noreferrer" target="_blank">
                    <button class="btn btn-primary btn-lg w-100" type="button">
                        <i class="bi-box-arrow-up-right flex-shrink-0 me-2"></i>
                        Registration Form
                    </button>
                </a>
            </div>

        </div>

        <div class="col col-sm-8 py-lg-5 mx-auto">
            <div class="video-embed ratio ratio-16x9">
                <iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen frameborder="0" src="https://www.youtube.com/embed/pWK_QZkIbQ0"></iframe>
            </div>
        </div>

    </div>
</div>

<div class="container-md py-4">
    <h2 class="display-4">Fees Structure</h2>
    <div class="table-responsive">
        <table class="align-middle">
            <thead>
                {% for item in site.data.fees.headers %}
                    <th class="bg-red" scope="col">
                        {{item}}
                    </th>
                {% endfor %}
            </thead>
            <tbody class="table-group-divider">
                {% for rows in site.data.fees.rows %}
                    <tr>
                        {% assign first_item = rows.row.first %}
                        {% for item in rows.row %}
                            {% if item == first_item %}
                                <th>{{item}}</th>
                            {% else %}
                                <td>{{item}}</td>
                            {% endif %}
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>

<div class="container-md py-4">
    <h2 class="display-4">Optional</h2>
    <div class="table-responsive">
        <table class="align-middle">
            <thead>
                {% for item in site.data.fees-optional.headers %}
                    <th class="bg-blue" scope="col">
                        {{item}}
                    </th>
                {% endfor %}
            </thead>
            <tbody class="table-group-divider">
                {% for rows in site.data.fees-optional.rows %}
                    <tr>
                        {% assign first_item = rows.row.first %}
                        {% for item in rows.row %}
                            {% if item == first_item %}
                                <th>{{item}}</th>
                            {% else %}
                                <td>{{item}}</td>
                            {% endif %}
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
