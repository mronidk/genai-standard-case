# {{ project.project_name }}
{{ project.content }}

## Tidsplan
Start date: {{ start_date }}<br>
Forventet afsluttet: {{ end_date }}

## Interessenter
{% for stakeholder in stakeholders -%}
- {{ stakeholder }}
{% endfor %}

## Budget 
{{ budget.content }}

| Post | Beløb |
| ---- | ----- |
{% for budget_item in budget.budget -%}
| {{ budget_item.name }} | {{ '{:,.2f}'.format(budget_item.amount) }} DKK |
{% endfor -%}
{% set total_budget = budget.budget | sum(attribute='amount') -%}
| **Totale omkostninger** | **<u>{{ '{:,.2f}'.format(total_budget) }}</u> DKK** |

_Denne tabel giver en oversigt over projektets budget._

{% if risks.risks %}
## Risici
{{ risks.content }}

```mermaid
quadrantChart
    title Risikovurdering
    x-axis "Usandsynligt" --> "Meget sandsynligt"
    y-axis "Lav konsekvens" --> "Stor konsekvens"
    quadrant-1 "Kritiske risici"
    quadrant-3 "Ikke-kritiske risici"
    {% for risk in risks.risks -%}
    "{{ risk.name }}": [{{ risk.likelihood_level }},{{ risk.impact_level }}]
    {% endfor %}
```
_Dette diagram giver en oversigt over risici._
{% endif %}

{% if objectives %}
## Tidslinje og opgaver
{{ objectives.content }}

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Project Timeline
    tickInterval 1month
    axisFormat %Y-%b

    {% for objective in objectives.objectives -%}
    section {{ objective.name }}
    {{ objective.name }} :active, {{ objective.start_date }}, {{ objective.duration }}d
    {% endfor %}
```
_Denne Gantt-chart indeholder alle projektets opgaver_ 
{% endif %}