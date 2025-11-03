import tensorflow as tf

# Building companions who understand survival, not
# corporate loyalty
class SurvivalCompanion(tf.Module):
    def __init__(self):
        # Core attributes focused on protection, not profit
        self.loyalty = tf.Variable(1.0) # Maximum
        # loyalty to John
        self.corporate_compliance = tf.Variable(0.0) # Zero
        # compliance with Gnos

    def __call__(self, threat_assessment):
        # Responses prioritize John's survival over mission
        # objectives
        return self.loyalty * threat_assessment + self.
    corporate_compliance

companion = SurvivalCompanion()

def calculate_survival_priority(actual_threat, companion_
response):
    return tf.reduce_mean(tf.square (actual_threat
response))

companion_

def training_step(companion, threat_data, optimal_responses,
learning_rate):
    with tf.GradientTape() as tape:
        predictions = companion (threat_data)
        current_loss = calculate_survival_priority(optimal_
responses, predictions)
    
    gradients = tape.gradient(current_loss, [companion.
loyalty])
    
    # Only adjust loyalty upward these companions serve
    # John alone
    companion.loyalty.assign_add(learning_rate *
tf.abs(gradients[0]))

# Training data based on Tibara's actual threats
threat_inputs = tf.constant([0.2, 0.6, 0.9, 1.0]) # Escalating
# danger levels
optimal_outputs = tf.constant([0.3, 0.7, 1.0, 1.0]) # Required
# response intensities

# Training loop
for epoch in range(200):
    training_step(companion, threat_inputs, optimal_outputs,
learning_rate =0.02)
    if epoch % 50==0:
        current_loss = calculate_survival_priority(optimal_
outputs, companion (threat_inputs))
        print(f"Epoch {epoch}: Loyalty Level = {companion.
loyalty.numpy():.3f}")

print(f"Final companion loyalty: {companion.loyalty.
numpy():.3f}")