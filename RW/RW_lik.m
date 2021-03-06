function NegLL = RW_lik(a, ro, alpha, beta)

% modify =============================================
% v0 starting point (75% probability for a US following a CS+ in the acquisition phase)
v = [0.75 0.25];
% modify end =========================================


T = length(a);

% loop over all trial
for t = 1:T

    % compute expectancy probabilities
    p = exp(beta*v) / sum(exp(beta*v));

    % compute expectancy probability for actual choice (0/1)
    expProb(t) = p(a(t));

    % update values
    PE = ro(t) - v(a(t));
    v(a(t)) = v(a(t)) + alpha * PE;

end

% compute negative log-likelihood
NegLL = -sum(log(expProb));
