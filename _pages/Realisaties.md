---
layout: page
title: Realisaties
permalink: /Realisaties
order: 1
---

{%- if site.projects.size > 0 -%}
  <!-- <h2 class="post-list-heading">{{ page.list_title | default: "Posts" }}</h2> -->
  <ul class="post-list">
    {%- for post in site.projects -%}
    <li>
      {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
      <!-- <span class="post-meta">{{ post.date | date: date_format }}</span> -->
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.location | escape }}: {{ post.title | escape }}
        </a>
      </h3>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
      {%- endif -%}
    </li>
    {%- endfor -%}
  </ul>
{%- endif -%}