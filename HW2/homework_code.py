import CONSTANTS

class BiddingAgent1:
    def get_bid(self, num_of_agents, P, q, v):
        if not hasattr(self, "boost"):
            self.boost = 1.04
            self.loss_streak = 0
            self.last_ctr = 0.3

        est_bid = v / 3.0
        q_opponent = q * 0.87
        avg_ctr = sum(P[:min(3, len(P))]) / min(len(P), 3) if len(P) > 0 else 0.3
        self.last_ctr = avg_ctr

        # תשלום צפוי לפי q
        est_payment = est_bid * q_opponent / max(q, 1e-9)
        smart_bid = v - (v - est_payment) * avg_ctr
        smart_bid *= self.boost

        # התאמה לפי מספר מתחרים – יותר סוכנים => יותר תחרות => טיפה יותר אגרסיבי
        smart_bid *= 1 + (0.01 * min(num_of_agents, 5))

        # קאפ לשמירה על רווח
        max_bid = 1.12 * v / 2.8
        bid = min(smart_bid, max_bid)
        return max(bid, CONSTANTS.MIN_PAYMENT)

    def notify_outcome(self, reward, payment, position):
        if not hasattr(self, "boost"):
            self.boost = 1.04
            self.loss_streak = 0

        if position < 0:
            self.loss_streak += 1
            if self.loss_streak >= 2 and self.boost < 1.12:
                self.boost += 0.015
                self.loss_streak = 0
        else:
            self.loss_streak = 0
            if self.boost > 1.01:
                self.boost -= 0.005

    def get_id(self):
        return "id_213690928_325468510"


class BiddingAgent2:
    def get_bid(self, num_of_agents, P, q, v):
        if not hasattr(self, "boost"):
            self.boost = 1.07
            self.loss_streak = 0
            self.last_ctr = 0.3

        est_bid = v / 2.7
        q_opponent = q * 0.9
        avg_ctr = sum(P[:2]) / 2 if len(P) >= 2 else 0.3
        self.last_ctr = avg_ctr

        est_payment = est_bid * q_opponent / max(q, 1e-9)
        smart_bid = v - (v - est_payment) * avg_ctr
        smart_bid *= self.boost

        if num_of_agents > 5:
            smart_bid *= 1.02

        max_bid = 1.17 * v / 2.7
        bid = min(smart_bid, max_bid)
        return max(bid, CONSTANTS.MIN_PAYMENT)

    def notify_outcome(self, reward, payment, position):
        if not hasattr(self, "boost"):
            self.boost = 1.07
            self.loss_streak = 0

        if position < 0:
            self.loss_streak += 1
            if self.loss_streak >= 2 and self.boost < 1.18:
                self.boost += 0.02
                self.loss_streak = 0
        else:
            self.loss_streak = 0
            if self.boost > 1.02:
                self.boost -= 0.006

    def get_id(self):
        return "id_213690928_325468510"
