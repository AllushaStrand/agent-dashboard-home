from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def job_agent(request):
    output = None

    if request.method == "POST":
        job_description = request.POST.get("job_description", "")
        jd = job_description.lower()

        # =========================
        # 1. HARD FILTERS
        # =========================

        if "no sponsorship" in jd:
            output = "Decision: SKIP\nReason: No visa sponsorship"

        elif "australian citizen" in jd or "permanent resident" in jd:
            output = "Decision: SKIP\nReason: Requires PR/citizen"

        else:
            # =========================
            # PRODUCT ROLE DETECTION
            # =========================

            product_role_terms = [
                "product manager",
                "product owner",
                "head of product",
                "product lead",
            ]

            product_signals = [
                "roadmap",
                "product strategy",
                "stakeholders",
                "delivery",
                "customer",
            ]

            is_product_role = any(term in jd for term in product_role_terms)
            has_product_signals = sum(1 for s in product_signals if s in jd) >= 2

            if not is_product_role and not has_product_signals:
                output = "Decision: SKIP\nReason: Not a product role"

            else:
                # =========================
                # SCORING
                # =========================

                score = 0
                breakdown = []

                if "saas" in jd:
                    score += 4
                    breakdown.append("+4 SaaS")

                if "api" in jd or "integration" in jd:
                    score += 1
                    breakdown.append("+1 API")

                if "data" in jd:
                    score += 2
                    breakdown.append("+2 Data")

                if "ai" in jd or "automation" in jd:
                    score += 2
                    breakdown.append("+2 AI")

                if "8 years" in jd or "10 years" in jd:
                    score -= 4
                    breakdown.append("-4 Too senior")

                # =========================
                # DECISION
                # =========================

                if score >= 8:
                    decision = "APPLY"
                elif score >= 5:
                    decision = "MAYBE"
                else:
                    decision = "SKIP"

                output = f"""
Decision: {decision}
Score: {score}

Breakdown:
{chr(10).join(breakdown)}
"""

    return render(request, "agents/job_agent.html", {
        "output": output
    })