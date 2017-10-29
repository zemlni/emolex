import pickle

emotions = {0 : ['Terror', 'Fear', 'Apprehension'],
            22.5 : ['Wonder', 'Paranoia', 'Worry'],
            45 : ['Admiration', 'Trust', 'Acceptance'],
            67.5 : ['Adoration', 'Love', 'Contentment'],
            90 : ['Ecstasy', 'Joy', 'Serenity'],
            112.5 : ['Envy', 'Vulnerability', 'Resignation'],
            135 : ['Vigilance', 'Anticipation', 'Interest'],
            157.5 : ['Hopelessness', 'Despair', 'Anxiety'],
            180 : ['Rage', 'Anger', 'Annoyance'],
            202.5 : ['Dread', 'Excitement', 'Curiosity'],
            225 : ['Loathing', 'Disgust', 'Boredom'],
            247.5 : ['Cruel', 'Hatred', 'Disgruntled'],
            270 : ['Grief', 'Sadness', 'Pensiveness'],
            292.5 : ['Resentment', 'Broodiness', 'Apathy'],
            315 : ['Amazement', 'Surprise', 'Distraction'],
            337.5 : ['Hopeful', 'Melancholy', 'Dismay']
            }

pickle.dump(emotions, open("emotions", "wb+"))
