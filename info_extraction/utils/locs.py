import numpy as np
from .fill_forms import make_name, make_email, make_date, make_number, make_country

def pick_x(middle, dist=50):
    choices = np.arange(middle - dist, middle + dist)
    x = np.random.choice(choices)
    return x

def maybe_add_alias(l, l_text, loc, prob=0.15):
    if np.random.uniform() < prob:
        l.append(loc)
        l_text.append(make_name())
        return True

def make_d1v1p1():
    locs = [
        [pick_x(576, 450), 705], [pick_x(1624, 400), 705], [pick_x(401, 200), 805], [pick_x(1100, 200), 805], [pick_x(576, 450), 965], [pick_x(1624, 450), 965], [pick_x(576, 450), 1065],
    ]
    locs_text = [
        make_name(), make_name(), make_number(), make_country(), make_number(), make_email(), make_number()
    ]
    entities = [
        'First Name', 'Last Name', 'Passport', 'Issuing Country', 'Home Phone', 'Personal Email', 'Mobile Phone'
    ]
    visa_number = [pick_x(1799, 200), 805]
    visa_number_text = make_number()
    if np.random.uniform() < 0.15:
        locs.append(visa_number)
        locs_text.append(visa_number_text)
        entities.append('Visa Number')
    professional_email = [pick_x(1624, 450), 1065]
    professional_email_text = make_email()
    if np.random.uniform() < 0.35:
        locs.append(professional_email)
        locs_text.append(professional_email_text)
        entities.append('Professional Email')
    spouse = [
        [pick_x(490), 1344], [pick_x(763), 1344], [pick_x(1256), 1344], [pick_x(1492), 1344], [pick_x(1728), 1344], [pick_x(1996), 1344],
    ]
    spouse_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    spouse_entities = ['Spouse First Name', 'Spouse Last Name', 'Spouse Birthplace', 'Spouse Birthdate', 'Spouse ID', "Spouse's Father"]
    added = maybe_add_alias(spouse, spouse_text, [pick_x(1017), 1344], 0.3)
    if added:
        spouse_entities.append('Spouse Aliases')
    if np.random.uniform() < 0.3:
        locs += spouse
        locs_text += spouse_text
        entities += spouse_entities
    mother = [
        [pick_x(490), 1414], [pick_x(763), 1414], [pick_x(1256), 1414], [pick_x(1492), 1414], [pick_x(1728), 1414], [pick_x(1996), 1414],
    ]
    mother_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    mother_entities = ['Mother First Name', 'Mother Last Name', 'Mother Birthplace', 'Mother Birthdate', 'Mother ID', "Mother's Father"]
    added = maybe_add_alias(mother, mother_text, [pick_x(1017), 1414], 0.4)
    if added:
        mother_entities.append('Mother Aliases')
    locs += mother
    locs_text += mother_text
    entities += mother_entities
    father = [
        [pick_x(490), 1484],[pick_x(763), 1484],[pick_x(1256), 1484],[pick_x(1492), 1484],[pick_x(1728), 1484],[pick_x(1996), 1484],
    ]
    father_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    father_entities = ['Father First Name', 'Father Last Name', 'Father Birthplace', 'Father Birthdate', 'Father ID', "Father's Father"]
    added = maybe_add_alias(father, father_text, [pick_x(1017), 1484], 0.15)
    if added:
        father_entities.append('Father Aliases')
    locs += father
    locs_text += father_text
    entities += father_entities
    step_mother = [
        [pick_x(490), 1554], [pick_x(763), 1554], [pick_x(1256), 1554], [pick_x(1492), 1554], [pick_x(1728), 1554], [pick_x(1996), 1554],
    ]
    step_mother_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    step_mother_entities = ['Step Mother First Name', 'Step Mother Last Name', 'Step Mother Birthplace', 'Step Mother Birthdate', 'Step Mother ID', "Step Mother's Father"]
    added = maybe_add_alias(step_mother, step_mother_text, [pick_x(1017), 1554], 0.35)
    if added:
        step_mother_entities.append('Step Mother Aliases')
    if np.random.uniform() < 0.4:
        locs += step_mother
        locs_text += step_mother_text
        entities += step_mother_entities

    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d1v1p2():
    locs = []
    locs_text = []
    entities = []
    if np.random.uniform() < 0.15:
        locs += [
            [pick_x(490), 161],[pick_x(763), 161],[pick_x(1256), 161],[pick_x(1492), 161],[pick_x(1728), 161],[pick_x(1996), 161],
            [pick_x(860), 1408], [pick_x(1360), 1408], [pick_x(1879), 1408],
        ]
        locs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name(), make_number(), make_number(), make_email(),
        ]
        entities += [
            'Step Father First Name', 'Step Father Last Name', 'Step Father Birthplace', 'Step Father Birthdate', 'Step Father ID', 
            "Step Father's Father", 'Step Father Mobile Phone', 'Step Father Home Phone', 'Step Father Email'
        ]
        added = maybe_add_alias(locs, locs_text, [pick_x(1017), 161])
        if added:
            entities.append('Step Father Alias')
    u = np.random.uniform()
    sibs = []
    sibs_text = []
    sibs_entities = []
    if u < 0.75:
        sibs += [
            [pick_x(490), 231], [pick_x(763), 231], [pick_x(1256), 231],[pick_x(1492), 231],[pick_x(1728), 231],[pick_x(1996), 231],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 1 First Name', 'Sibling 1 Last Name', 'Sibling 1 Birthplace', 'Sibling 1 Birthdate', 'Sibling 1 ID', "Sibling 1's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 231], 0.1)
        if added:
            sibs_entities.append('Sibling 1 Alias')
    if u < 0.55:
        sibs += [
            [pick_x(490), 301], [pick_x(763), 301], [pick_x(1256), 301], [pick_x(1492), 301], [pick_x(1728), 301], [pick_x(1996), 301],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 2 First Name', 'Sibling 2 Last Name', 'Sibling 2 Birthplace', 'Sibling 2 Birthdate', 'Sibling 2 ID', "Sibling 2's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 301], 0.1)
        if added:
            sibs_entities.append('Sibling 2 Alias')
    if u < 0.3:
        sibs += [
            [pick_x(490), 371],[pick_x(763), 371],[pick_x(1256), 371],[pick_x(1492), 371],[pick_x(1728), 371],[pick_x(1996), 371],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 3 First Name', 'Sibling 3 Last Name', 'Sibling 3 Birthplace', 'Sibling 3 Birthdate', 'Sibling 3 ID', "Sibling 3's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 371], 0.1)
        if added:
            sibs_entities.append('Sibling 3 Alias')
    if u < 0.15:
        sibs += [
            [pick_x(490), 441],[pick_x(763), 441],[pick_x(1256), 441],[pick_x(1492), 441],[pick_x(1728), 441],[pick_x(1996), 441],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 4 First Name', 'Sibling 4 Last Name', 'Sibling 4 Birthplace', 'Sibling 4 Birthdate', 'Sibling 4 ID', "Sibling 4's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 441], 0.1)
        if added:
            sibs_entities.append('Sibling 4 Alias')
    u = np.random.uniform()
    children = []
    children_text = []
    children_entities = []
    if u < 0.4:
        children += [
            [pick_x(490), 511],[pick_x(763), 511],[pick_x(1256), 511],[pick_x(1492), 511],[pick_x(1728), 511],[pick_x(1996), 511],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 1 First Name', 'Child 1 Last Name', 'Child 1 Birthplace', 'Child 1 Birthdate', 'Child 1 ID', "Child 1's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 511], 0.1)
        if added:
            children_entities.append('Child 1 Alias')
    if u < 0.3:
        children += [
            [pick_x(490), 581],[pick_x(763), 581],[pick_x(1256), 581],[pick_x(1492), 581],[pick_x(1728), 581],[pick_x(1996), 581],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 2 First Name', 'Child 2 Last Name', 'Child 2 Birthplace', 'Child 2 Birthdate', 'Child 2 ID', "Child 2's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 581], 0.1)
        if added:
            children_entities.append('Child 2 Alias')
    if u < 0.15:
        children += [
            [pick_x(490), 651],[pick_x(763), 651],[pick_x(1256), 651],[pick_x(1492), 651],[pick_x(1728), 651],[pick_x(1996), 651],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 3 First Name', 'Child 3 Last Name', 'Child 3 Birthplace', 'Child 3 Birthdate', 'Child 3 ID', "Child 3's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 651], 0.1)
        if added:
            children_entities.append('Child 3 Alias')
    if u < 0.05:
        children += [
            [pick_x(490), 721],[pick_x(763), 721],[pick_x(1256), 721],[pick_x(1492), 721],[pick_x(1728), 721],[pick_x(1996), 721],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 4 First Name', 'Child 4 Last Name', 'Child 4 Birthplace', 'Child 4 Birthdate', 'Child 4 ID', "Child 4's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 721], 0.1)
        if added:
            children_entities.append('Child 4 Alias')
    if np.random.uniform() < 0.3:
        locs += [
            [pick_x(860), 1078], [pick_x(1360), 1078], [pick_x(1879), 1078],
        ]
        locs_text += [make_number(), make_number(), make_email()]
        entities += ['Spouse Mobile Phone', 'Spouse Home Phone', 'Spouse Email']
    locs += [
        [pick_x(860), 1160], [pick_x(1360), 1160], [pick_x(1879), 1160],
        [pick_x(860), 1243], [pick_x(1360), 1243], [pick_x(1879), 1243],
    ]
    locs_text += [
        make_number(), make_number(), make_email(), make_number(), make_number(), make_email()
    ]
    entities += ['Mother Mobile Phone', 'Mother Home Phone', 'Mother Email', 'Father Mobile Phone', 'Father Home Phone', 'Father Email']
    if np.random.uniform() < 0.15:
        locs += [
            [pick_x(860), 1325], [pick_x(1360), 1325], [pick_x(1879), 1325],
        ]
        locs_text += [make_number(), make_number(), make_email()]
        entities += ['Step Mother Mobile Phone', 'Step Mother Home Phone', 'Step Mother Email']
    locs += children
    locs_text += children_text
    entities += children_entities
    locs += sibs
    locs_text += sibs_text
    entities += sibs_entities

    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d1v1p3():
    locs = [   
        [pick_x(201), 180+13], [pick_x(650, 200), 180+13], [pick_x(1250, 250), 180+13], [pick_x(1849, 150), 180+13], [pick_x(251), 280+13], 
        [pick_x(650, 100), 280+13], [pick_x(1499, 500), 280+13], [pick_x(1100, 1000), 380+13], [pick_x(576, 400), 480+13], [pick_x(1624, 400), 480+13],        
    ]
    locs_text = [make_date(), make_country(), make_name(), make_name(), make_number(), make_number(), make_country(), make_date(True), make_name(), make_name()]
    entities = ['Birthdate', 'Birth Country', 'Birth City', 'Residence', 'National ID', 'Military ID', 'Citizenship', 'College Attendance', 'Program', 'Degree']
    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d1v2p1():
    locs = [
        [pick_x(653, 320), 766+11],
        [pick_x(1524, 320), 766+11],
        [pick_x(508, 200), 842+11],
        [pick_x(1089, 200), 842+11], 
        [pick_x(653, 400), 962+11],
        [pick_x(1524, 400), 962+11],
        [pick_x(653, 400), 1038+11],
    ]
    locs_text = [
        make_name(), make_name(), make_number(), make_country(), make_number(), make_email(), make_number()
    ]
    entities = [
        'First Name', 'Last Name', 'Passport', 'Issuing Country', 'Home Phone', 'Personal Email', 'Mobile Phone'
    ]
    visa_number = [pick_x(1670, 200), 842+11]
    visa_number_text = make_number()
    professional_email = [pick_x(1524, 400), 1038+11]
    professional_email_text = make_email()
    spouse = [
        [pick_x(582, 50), 1261],
        [pick_x(808, 50), 1261],
        [pick_x(1219, 50), 1261],
        [pick_x(1414, 50), 1261],
        [pick_x(1611, 50), 1261],
        [pick_x(1833, 50), 1261],
    ]
    spouse_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    spouse_entities = ['Spouse First Name', 'Spouse Last Name', 'Spouse Birthplace', 'Spouse Birthdate', 'Spouse ID', "Spouse's Father"]
    added = maybe_add_alias(spouse, spouse_text, [pick_x(1020, 50), 1261], 0.3)
    if added:
        spouse_entities.append('Spouse Aliases')
    mother = [
        [pick_x(582, 50), 1314],
        [pick_x(808, 50), 1314],
        [pick_x(1219, 50), 1314],
        [pick_x(1414, 50), 1314],
        [pick_x(1611, 50), 1314],
        [pick_x(1833, 50), 1314],
    ]
    mother_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    mother_entities = ['Mother First Name', 'Mother Last Name', 'Mother Birthplace', 'Mother Birthdate', 'Mother ID', "Mother's Father"]
    added = maybe_add_alias(mother, mother_text, [pick_x(1020, 50), 1314], 0.4)
    if added:
        mother_entities.append('Mother Aliases')
    father = [
        [pick_x(582, 50), 1366],
        [pick_x(808, 50), 1366],
        [pick_x(1219, 50), 1366],
        [pick_x(1414, 50), 1366],
        [pick_x(1611, 50), 1366],
        [pick_x(1833, 50), 1366],
    ]
    father_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    father_entities = ['Father First Name', 'Father Last Name', 'Father Birthplace', 'Father Birthdate', 'Father ID', "Father's Father"]
    added = maybe_add_alias(father, father_text, [pick_x(1020, 50), 1366], 0.2)
    if added:
        father_entities.append('Father Aliases')
    step_mother = [
        [pick_x(582, 50), 1420],
        [pick_x(808, 50), 1420],
        [pick_x(1219, 50), 1420],
        [pick_x(1414, 50), 1420],
        [pick_x(1611, 50), 1420],
        [pick_x(1833, 50), 1420],  
    ]
    step_mother_text = [make_name(), make_name(), make_country(), make_date(), make_number(), make_name()]
    step_mother_entities = ['Step Mother First Name', 'Step Mother Last Name', 'Step Mother Birthplace', 'Step Mother Birthdate', 'Step Mother ID', "Step Mother's Father"]
    added = maybe_add_alias(step_mother, step_mother_text, [pick_x(1020, 50), 1420], 0.3)
    if added:
        step_mother_entities.append('Step Mother Aliases')
    locs += mother
    locs_text += mother_text
    entities += mother_entities
    locs += father
    locs_text += father_text
    entities += father_entities
    if np.random.uniform() < 0.15:
        locs.append(visa_number)
        locs_text.append(visa_number_text)
        entities.append('Visa Number')
    if np.random.uniform() < 0.35:
        locs.append(professional_email)
        locs_text.append(professional_email_text)
        entities.append('Professional Email')
    if np.random.uniform() < 0.3:
        locs += spouse
        locs_text += spouse_text
        entities += spouse_entities
    if np.random.uniform() < 0.15:
        locs += step_mother
        locs_text += step_mother_text
        entities += step_mother_entities
    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d1v2p2():
    def pick_x(middle, dist=50):
        choices = np.arange(middle - dist, middle + 5)
        x = np.random.choice(choices)
        return x
    locs = []
    locs_text = []
    entities = []
    if np.random.uniform() < 0.15:
        locs += [
            [pick_x(581), 324],[pick_x(807), 324],[pick_x(1215), 324],[pick_x(1411), 324],[pick_x(1607), 324],[pick_x(1828), 324],
            [pick_x(886), 1276],[pick_x(1301), 1276],[pick_x(1731), 1276],
        ]
        locs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name(), make_number(), make_number(), make_email(),
        ]
        entities += [
            'Step Father First Name', 'Step Father Last Name', 'Step Father Birthplace', 'Step Father Birthdate', 'Step Father ID', "Step Father's Father",
            'Step Father Mobile Phone', 'Step Father Home Phone', 'Step Father Email'
        ]
        added = maybe_add_alias(locs, locs_text, [pick_x(1017), 324])
        if added:
            entities.append('Step Father Alias')
    u = np.random.uniform()
    sibs = []
    sibs_text = []
    sibs_entities = []
    if u < 0.75:
        sibs += [
            [pick_x(581), 377],[pick_x(807), 377],[pick_x(1215), 377],[pick_x(1411), 377],[pick_x(1607), 377],[pick_x(1828), 377],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 1 First Name', 'Sibling 1 Last Name', 'Sibling 1 Birthplace', 'Sibling 1 Birthdate', 'Sibling 1 ID', "Sibling 1's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 377], 0.1)
        if added:
            sibs_entities.append('Sibling 1 Alias')
    if u < 0.55:
        sibs += [
            [pick_x(581), 431],[pick_x(807), 431],[pick_x(1215), 431],[pick_x(1411), 431],[pick_x(1607), 431],[pick_x(1828), 431],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 2 First Name', 'Sibling 2 Last Name', 'Sibling 2 Birthplace', 'Sibling 2 Birthdate', 'Sibling 2 ID', "Sibling 2's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 431], 0.1)
        if added:
            sibs_entities.append('Sibling 2 Alias')
    if u < 0.3:
        sibs += [
            [pick_x(581), 484],[pick_x(807), 484],[pick_x(1215), 484],[pick_x(1411), 484],[pick_x(1607), 484],[pick_x(1828), 484],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 3 First Name', 'Sibling 3 Last Name', 'Sibling 3 Birthplace', 'Sibling 3 Birthdate', 'Sibling 3 ID', "Sibling 3's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 484], 0.1)
        if added:
            sibs_entities.append('Sibling 3 Alias')
    if u < 0.15:
        sibs += [
            [pick_x(581), 537],[pick_x(807), 537],[pick_x(1215), 537],[pick_x(1411), 537],[pick_x(1607), 537],[pick_x(1828), 537],
        ]
        sibs_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 4 First Name', 'Sibling 4 Last Name', 'Sibling 4 Birthplace', 'Sibling 4 Birthdate', 'Sibling 4 ID', "Sibling 4's Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1017), 537], 0.1)
        if added:
            sibs_entities.append('Sibling 4 Alias')
    u = np.random.uniform()
    children = []
    children_text = []
    children_entities = []
    if u < 0.4:
        children += [
            [pick_x(581), 590],[pick_x(807), 590],[pick_x(1215), 590],[pick_x(1411), 590],[pick_x(1607), 590],[pick_x(1828), 590],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 1 First Name', 'Child 1 Last Name', 'Child 1 Birthplace', 'Child 1 Birthdate', 'Child 1 ID', "Child 1's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 590], 0.1)
        if added:
            children_entities.append('Child 1 Alias')
    if u < 0.3:
        children += [
            [pick_x(581), 643],[pick_x(807), 643],[pick_x(1215), 643],[pick_x(1411), 643],[pick_x(1607), 643],[pick_x(1828), 643],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 2 First Name', 'Child 2 Last Name', 'Child 2 Birthplace', 'Child 2 Birthdate', 'Child 2 ID', "Child 2's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 643], 0.1)
        if added:
            children_entities.append('Child 2 Alias')
    if u < 0.15:
        children += [
            [pick_x(581), 699],[pick_x(807), 699],[pick_x(1215), 699],[pick_x(1411), 699],[pick_x(1607), 699],[pick_x(1828), 699],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 3 First Name', 'Child 3 Last Name', 'Child 3 Birthplace', 'Child 3 Birthdate', 'Child 3 ID', "Child 3's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 699], 0.1)
        if added:
            children_entities.append('Child 3 Alias')
    if u < 0.05:
        children += [
            [pick_x(581), 752],[pick_x(807), 752],[pick_x(1215), 752],[pick_x(1411), 752],[pick_x(1607), 752],[pick_x(1828), 752],
        ]
        children_text += [
            make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += ['Child 4 First Name', 'Child 4 Last Name', 'Child 4 Birthplace', 'Child 4 Birthdate', 'Child 4 ID', "Child 4's Father"]
        added = maybe_add_alias(children, children_text, [pick_x(1017), 752], 0.1)
        if added:
            children_entities.append('Child 4 Alias')
    if np.random.uniform() < 0.3:
        locs += [
            [pick_x(886), 1024],[pick_x(1301), 1024],[pick_x(1731), 1024],
        ]
        locs_text += [make_number(), make_number(), make_email()]
        entities += ['Spouse Mobile Phone', 'Spouse Home Phone', 'Spouse Email']
    locs += [
        [pick_x(886), 1087],[pick_x(1301), 1087],[pick_x(1731), 1087],
        [pick_x(886), 1150],[pick_x(1301), 1150],[pick_x(1731), 1150],
    ]
    locs_text += [
        make_number(), make_number(), make_email(), make_number(), make_number(), make_email()
    ]
    entities += [
        'Mother Mobile Phone', 'Mother Home Phone', 'Mother Email', 'Father Mobile Phone', 'Father Home Phone', 'Father Email'
    ]
    if np.random.uniform() < 0.15:
        locs += [
            [pick_x(886), 1213],[pick_x(1301), 1213],[pick_x(1731), 1213],
        ]
        locs_text += [make_number(), make_number(), make_email()]
        entities += ['Step Mother Mobile Phone', 'Step Mother Home Phone', 'Step Mother Email']
    locs += children
    locs_text += children_text
    entities += children_entities
    locs += sibs
    locs_text += sibs_text
    entities += sibs_entities

    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d2v1p1():
    locs = [
        [pick_x(576, 400), 460+15],
        [pick_x(1624, 400), 460+15],
        [pick_x(401, 200), 560+15],
        [pick_x(1100, 200), 560+15],
        [pick_x(576, 400), 712+15],
        [pick_x(1624, 400), 712+15],
        [pick_x(576, 400), 812+15],
        [pick_x(860), 1560],
        [pick_x(1360, 150), 1560],
        [pick_x(1879, 150), 1560],
    ]
    locs_text = [
        make_name(), make_name(), make_number(), make_country(), make_number(),
        make_email(), make_number(), make_number(), make_number(), make_email(),
    ]
    entities = [
        'First Name', 'Last Name', 'Passport', 'Issuing Country', 'Home Phone', 'Personal Email', 'Mobile Phone',
        'Mother Mobile Phone', 'Mother Home Phone', 'Mother Email'
    ]
    visa_number = [pick_x(1799, 200), 560+15]
    visa_number_text = make_number()
    professional_email = [pick_x(1624, 400), 812+15]
    professional_email_text = make_email()
    if np.random.uniform() < 0.15:
        locs.append(visa_number)
        locs_text.append(visa_number_text)
        entities.append('Visa Number')
    if np.random.uniform() < 0.35:
        locs.append(professional_email)
        locs_text.append(professional_email_text)
        entities.append('Professional Email')
    u = np.random.uniform()
    if u < 0.9:
        locs += [
            [pick_x(251, 100), 1014],
            [pick_x(575), 1014],
            [pick_x(825), 1014],
            [pick_x(1250, 150), 1014],
            [pick_x(1849, 150), 1014],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 1 Country', 'Service 1 Start', 'Service 1 End', 'Service 1 Title', 'Service 1 Certificiation'
        ]
    if u < 0.8:
        locs += [
            [pick_x(251), 1058],
            [pick_x(575), 1058],
            [pick_x(825), 1058],
            [pick_x(1250, 150), 1058],
            [pick_x(1849, 150), 1058],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 2 Country', 'Service 2 Start', 'Service 2 End', 'Service 2 Title', 'Service 2 Certificiation'
        ]
    if u < 0.65:
        locs += [
            [pick_x(251), 1102],
            [pick_x(575), 1102],
            [pick_x(825), 1102],
            [pick_x(1250, 150), 1102],
            [pick_x(1849, 150), 1102],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 3 Country', 'Service 3 Start', 'Service 3 End', 'Service 3 Title', 'Service 3 Certificiation'
        ]
    if u < 0.5:
        locs += [
            [pick_x(251), 1146],
            [pick_x(575), 1146],
            [pick_x(825), 1146],
            [pick_x(1250, 150), 1146],
            [pick_x(1849, 150), 1146],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 4 Country', 'Service 4 Start', 'Service 4 End', 'Service 4 Title', 'Service 4 Certificiation'
        ]
    if u < 0.35:
        locs += [
            [pick_x(251), 1192],
            [pick_x(575), 1192],
            [pick_x(825), 1192],
            [pick_x(1250, 150), 1192],
            [pick_x(1849, 150), 1192],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 5 Country', 'Service 5 Start', 'Service 5 End', 'Service 5 Title', 'Service 5 Certificiation'
        ]
    if u < 0.2:
        locs += [
            [pick_x(251), 1236],
            [pick_x(575), 1236],
            [pick_x(825), 1236],
            [pick_x(1250, 150), 1236],
            [pick_x(1849, 150), 1236],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 6 Country', 'Service 6 Start', 'Service 6 End', 'Service 6 Title', 'Service 6 Certificiation'
        ]
    if u < 0.1:
        locs += [
            [pick_x(251), 1280],
            [pick_x(575), 1280],
            [pick_x(825), 1280],
            [pick_x(1250, 150), 1280],
            [pick_x(1849, 150), 1280],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 7 Country', 'Service 7 Start', 'Service 7 End', 'Service 7 Title', 'Service 7 Certificiation'
        ]
    if np.random.uniform() < 0.35:
        locs += [
            [pick_x(860), 1520],
            [pick_x(1360, 150), 1520],
            [pick_x(1879, 150), 1520],
        ]
        locs_text += [
            make_number(), make_number(), make_email()
        ]
        entities += [
            'Spouse Mobile Phone', 'Spouse Home Phone', 'Spouse Email'
        ]
    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d2v1p2():
    def pick_x(middle, dist=20):
        choices = np.arange(middle - dist, middle + 5)
        x = np.random.choice(choices)
        return x
    locs = []
    locs_text = []
    entities = []
    mother = [
        [pick_x(581), 440],[pick_x(832), 440],[pick_x(1317), 440],[pick_x(1538), 440],[pick_x(1758), 440],[pick_x(2012), 440],
    ]
    mother_text = [
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    mother_entities = [
        'Mother First Name', 'Mother Last Name', 'Mother Birthplace', 'Mother Birthdate', 'Mother ID', "Mother's Father"
    ]
    added = maybe_add_alias(mother, mother_text, [pick_x(1078), 440], 0.35)
    if added:
        mother_entities.append('Mother Alias')
    locs += mother
    locs_text += mother_text
    entities += mother_entities
    father = [
        [pick_x(860, 100), 140],[pick_x(1360, 100), 140],[pick_x(1879, 100), 140],
        [pick_x(581), 480],[pick_x(832), 480],[pick_x(1317), 480],[pick_x(1538), 480],[pick_x(1758), 480],[pick_x(2012), 480],
    ]
    father_text = [
        make_number(), make_number(), make_email(), 
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    father_entities = [
        'Father Mobile Phone', 'Father Home Phone', 'Father Email',
        'Father First Name', 'Father Last Name', 'Father Birthplace', 'Father Birthdate', 'Father ID', "Father's Father"
    ]
    added = maybe_add_alias(father, father_text, [pick_x(1078), 480], 0.35)
    if added:
        father_entities.append('Father Alias')
    locs += father
    locs_text += father_text
    entities += father_entities
    spouse = [
        [pick_x(581), 398],[pick_x(832), 398],[pick_x(1317), 398],[pick_x(1538), 398],[pick_x(1758), 398],[pick_x(2012), 398],
    ]
    spouse_text = [
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    spouse_entities = [
        'Spouse First Name', 'Spouse Last Name', 'Spouse Birthplace', 'Spouse Birthdate', 'Spouse ID', "Spouse's Father"
    ]
    added = maybe_add_alias(spouse, spouse_text, [pick_x(1078), 398], 0.35)
    if added:
        spouse_entities.append('Spouse Alias')
    step_mother = [
        [pick_x(860, 100), 180],[pick_x(1360, 100), 180],[pick_x(1879, 100), 180],
        [pick_x(581), 520],[pick_x(832), 520],[pick_x(1317), 520],[pick_x(1538), 520],[pick_x(1758), 520],[pick_x(2012), 520],
    ]
    step_mother_text = [
        make_number(), make_number(), make_email(), 
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    step_mother_entities = [
        'Step Mother First Name', 'Step Mother Last Name', 'Step Mother Birthplace', 'Step Mother Birthdate', 'Step Mother ID', "Step Mother's Father"
    ]
    added = maybe_add_alias(step_mother, step_mother_text, [pick_x(1078), 520], 0.35)
    if added:
        step_mother_entities.append('Step Mother Alias')
    step_father = [
        [pick_x(860, 100), 220],[pick_x(1360, 100), 220],[pick_x(1879, 100), 220],
        [pick_x(581), 560],[pick_x(832), 560],[pick_x(1317), 560],[pick_x(1538), 560],[pick_x(1758), 560],[pick_x(2012), 560],
    ]
    step_father_text = [
        make_number(), make_number(), make_email(), 
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    step_father_entities = [
        'Step Father Mobile Phone', 'Step Father Home Phone', 'Step Father Email'
        'Step Father First Name', 'Step Father Last Name', 'Step Father Birthplace', 'Step Father Birthdate', 'Step Father ID', "Step Father's Father"
    ]
    added = maybe_add_alias(step_father, step_father_text, [pick_x(1078), 560], 0.3)
    if added:
        step_father_entities.append('Step Father Alias')
    if np.random.uniform() < 0.15:
        locs += step_father
        locs_text += step_father_text
        entities += step_father_entities
    u = np.random.uniform()
    sibs = []
    sibs_text = []
    sibs_entities = []
    if u < 0.75:
        sibs += [
            [pick_x(581), 600],[pick_x(832), 600],[pick_x(1317), 600],[pick_x(1538), 600],[pick_x(1758), 600],[pick_x(2012), 600],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 1 First Name', 'Sibling 1 Last Name', 'Sibling 1 Birthplace', 'Sibling 1 Birthdate', 'Sibling 1 ID', "Sibling 1 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1078), 600], 0.1)
        if added:
            sibs_entities.append('Sibling 1 Alias')
    if u < 0.55:
        sibs += [
            [pick_x(581), 640],[pick_x(832), 640],[pick_x(1317), 640],[pick_x(1538), 640],[pick_x(1758), 640],[pick_x(2012), 640],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 2 First Name', 'Sibling 2 Last Name', 'Sibling 2 Birthplace', 'Sibling 2 Birthdate', 'Sibling 2 ID', "Sibling 2 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1078), 640], 0.1)
        if added:
            sibs_entities.append('Sibling 2 Alias')
    if u < 0.3:
        sibs += [
            [pick_x(581), 680],[pick_x(832), 680],[pick_x(1317), 680],[pick_x(1538), 680],[pick_x(1758), 680],[pick_x(2012), 680],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 3 First Name', 'Sibling 3 Last Name', 'Sibling 3 Birthplace', 'Sibling 3 Birthdate', 'Sibling 3 ID', "Sibling 3 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1078), 680], 0.1)
        if added:
            sibs_entities.append('Sibling 3 Alias')
    if u < 0.15:
        sibs += [
            [pick_x(581), 720],[pick_x(832), 720],[pick_x(1317), 720],[pick_x(1538), 720],[pick_x(1758), 720],[pick_x(2012), 720],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 4 First Name', 'Sibling 4 Last Name', 'Sibling 4 Birthplace', 'Sibling 4 Birthdate', 'Sibling 4 ID', "Sibling 4 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1078), 720], 0.1)
        if added:
            sibs_entities.append('Sibling 4 Alias')
    u = np.random.uniform()
    children = []
    children_text = []
    children_entities = []
    if u < 0.4:
        children += [
            [pick_x(581), 760],[pick_x(832), 760],[pick_x(1317), 760],[pick_x(1538), 760],[pick_x(1758), 760],[pick_x(2012), 760],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 1 First Name', 'Child 1 Last Name', 'Child 1 Birthplace', 'Child 1 Birthdate', 'Child 1 ID', "Child 1 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1078), 760], 0.1)
        if added:
            children_entities.append('Child 1 Alias')
    if u < 0.3:
        children += [
            [pick_x(581), 800],[pick_x(832), 800],[pick_x(1317), 800],[pick_x(1538), 800],[pick_x(1758), 800],[pick_x(2012), 800],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 2 First Name', 'Child 2 Last Name', 'Child 2 Birthplace', 'Child 2 Birthdate', 'Child 2 ID', "Child 2 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1078), 800], 0.1)
        if added:
            children_entities.append('Child 2 Alias')
    if u < 0.15:
        children += [
             [pick_x(581), 840],[pick_x(832), 840],[pick_x(1317), 840],[pick_x(1538), 840],[pick_x(1758), 840],[pick_x(2012), 840],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 3 First Name', 'Child 3 Last Name', 'Child 3 Birthplace', 'Child 3 Birthdate', 'Child 3 ID', "Child 3 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1078), 840], 0.1)
        if added:
            children_entities.append('Child 3 Alias')
    if u < 0.05:
        children += [
            [pick_x(581), 880],[pick_x(832), 880],[pick_x(1317), 880],[pick_x(1538), 880],[pick_x(1758), 880],[pick_x(2012), 880],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 4 First Name', 'Child 4 Last Name', 'Child 4 Birthplace', 'Child 4 Birthdate', 'Child 4 ID', "Child 4 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1078), 880], 0.1)
        if added:
            children_entities.append('Child 4 Alias')
    u = np.random.uniform()
    countries = []
    countries_text = []
    countries_entities = []
    if u < 0.9:
        countries += [
             [pick_x(301), 1248],[pick_x(750),1248],[pick_x(1150),1248],[pick_x(1749, 200),1248],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 1 Country', 'Travel 1 Start', 'Travel 1 End', 'Travel 1 Names'
        ]
    if u < 0.8:
        countries += [
            [pick_x(301),1288],[pick_x(750),1288],[pick_x(1150),1288],[pick_x(1749, 200),1288],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 2 Country', 'Travel 2 Start', 'Travel 2 End', 'Travel 2 Names'
        ]
    if u < 0.6:
        countries += [
            [pick_x(301),1328],[pick_x(750),1328],[pick_x(1150),1328],[pick_x(1749, 200),1328],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 3 Country', 'Travel 3 Start', 'Travel 3 End', 'Travel 3 Names'
        ]
    if u < 0.5:
        countries += [
            [pick_x(301),1368],[pick_x(750),1368],[pick_x(1150),1368],[pick_x(1749, 200),1368],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 4 Country', 'Travel 4 Start', 'Travel 4 End', 'Travel 4 Names'
        ]
    if u < 0.4:
        countries += [
            [pick_x(301),1408],[pick_x(750),1408],[pick_x(1150),1408],[pick_x(1749, 200),1408],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 5 Country', 'Travel 5 Start', 'Travel 5 End', 'Travel 5 Names'
        ]
    if u < 0.3:
        countries += [
            [pick_x(301),1448],[pick_x(750),1448],[pick_x(1150),1448],[pick_x(1749, 200),1448],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 6 Country', 'Travel 6 Start', 'Travel 6 End', 'Travel 6 Names'
        ]
    if u < 0.2:
        countries += [
            [pick_x(301),1488],[pick_x(750),1488],[pick_x(1150),1488],[pick_x(1749, 200),1488],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 7 Country', 'Travel 7 Start', 'Travel 7 End', 'Travel 7 Names'
        ]
    if u < 0.1:
        countries += [
            [pick_x(301),1528],[pick_x(750),1528],[pick_x(1150),1528],[pick_x(1749, 200),1528],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 8 Country', 'Travel 8 Start', 'Travel 8 End', 'Travel 8 Names'
        ]
    if u < 0.05:
        countries += [
            [pick_x(301),1568],[pick_x(750),1568],[pick_x(1150),1568],[pick_x(1749, 200),1568],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 9 Country', 'Travel 9 Start', 'Travel 9 End', 'Travel 9 Names'
        ]
    locs += children
    locs_text += children_text
    entities += children_entities
    locs += sibs
    locs_text += sibs_text
    entities += sibs_entities
    locs += countries
    locs_text += countries_text
    entities += countries_entities
    if np.random.uniform() < 0.3:
        locs += spouse
        locs_text += spouse_text
        entities += spouse_entities
    if np.random.uniform() < 0.15:
        locs += step_mother
        locs_text += step_mother_text
        entities += step_mother_entities
    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)


def make_d2v2p1():
    def pick_x(middle, dist=20):
        choices = np.arange(middle - dist, middle + 5)
        x = np.random.choice(choices)
        return x
    locs = [
        [pick_x(652, 400), 591+8],[pick_x(1520, 400), 591+8],
        [pick_x(507, 200), 666+8],[pick_x(1086, 200), 666+8],
        [pick_x(652, 400), 785+8],[pick_x(1520, 400), 785+8],
        [pick_x(652, 400), 861+8],
        [pick_x(886), 1436],[pick_x(1300), 1436],[pick_x(1730), 1436],
    ]
    locs_text = [
        make_name(), make_name(), make_number(), make_country(), make_number(),
        make_email(), make_number(), make_number(), make_number(), make_email(),
    ]
    entities = [
        'First Name', 'Last Name', 'Passport', 'Issuing Country', 'Home Phone', 'Personal Email', 'Mobile Phone',
        'Mother Mobile Phone', 'Mother Home Phone', 'Mother Email'
    ]
    visa_number = [pick_x(1665, 200), 666+8]
    visa_number_text = make_number()
    professional_email = [pick_x(1520, 400), 861+8]
    professional_email_text = make_email()
    if np.random.uniform() < 0.15:
        locs.append(visa_number)
        locs_text.append(visa_number_text)
        entities.append('Visa Number')
    if np.random.uniform() < 0.35:
        locs.append(professional_email)
        locs_text.append(professional_email_text)
        entities.append('Professional Email')
    u = np.random.uniform()
    if u < 0.8:
        locs += [
            [pick_x(383), 1022],[pick_x(651), 1022],[pick_x(858), 1022],[pick_x(1209), 1022],[pick_x(1706), 1022],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 1 Country', 'Service 1 Start', 'Service 1 End', 'Service 1 Title', 'Service 1 Certificiation'
        ]
    if u < 0.7:
        locs += [
            [pick_x(383), 1055],[pick_x(651), 1055],[pick_x(858), 1055],[pick_x(1209), 1055],[pick_x(1706), 1055],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 2 Country', 'Service 2 Start', 'Service 2 End', 'Service 2 Title', 'Service 2 Certificiation'
        ]
    if u < 0.4:
        locs += [
            [pick_x(383), 1089],[pick_x(651), 1089],[pick_x(858), 1089],[pick_x(1209), 1089],[pick_x(1706), 1089],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 3 Country', 'Service 3 Start', 'Service 3 End', 'Service 3 Title', 'Service 3 Certificiation'
        ]
    if u < 0.35:
        locs += [
            [pick_x(383), 1122],[pick_x(651), 1122],[pick_x(858), 1122],[pick_x(1209), 1122],[pick_x(1706), 1122],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 4 Country', 'Service 4 Start', 'Service 4 End', 'Service 4 Title', 'Service 4 Certificiation'
        ]
    if u < 0.2:
        locs += [
            [pick_x(383), 1155],[pick_x(651), 1155],[pick_x(858), 1155],[pick_x(1209), 1155],[pick_x(1706), 1155],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 5 Country', 'Service 5 Start', 'Service 5 End', 'Service 5 Title', 'Service 5 Certificiation'
        ]
    if u < 0.14:
        locs += [
            [pick_x(383), 1189],[pick_x(651), 1189],[pick_x(858), 1189],[pick_x(1209), 1189],[pick_x(1706), 1189],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 6 Country', 'Service 6 Start', 'Service 6 End', 'Service 6 Title', 'Service 6 Certificiation'
        ]
    if u < 0.08:
        locs += [
            [pick_x(383), 1222],[pick_x(651), 1222],[pick_x(858), 1222],[pick_x(1209), 1222],[pick_x(1706), 1222],
        ]
        locs_text += [
            make_country(), make_date(True), make_date(True), make_name(), make_name()
        ]
        entities += [
            'Service 7 Country', 'Service 7 Start', 'Service 7 End', 'Service 7 Title', 'Service 7 Certificiation'
        ]
    if np.random.uniform() < 0.35:
        locs += [
           [pick_x(886), 1407],[pick_x(1300), 1407],[pick_x(1730), 1407],
        ]
        locs_text += [
            make_number(), make_number(), make_email()
        ]
        entities += [
            'Spouse Mobile Phone', 'Spouse Home Phone', 'Spouse Email'
        ]
    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)

def make_d2v2p2():
    def pick_x(middle, dist=30):
        choices = np.arange(middle - dist, middle + 5)
        x = np.random.choice(choices)
        return x
    locs = []
    locs_text = []
    entities = []
    mother = [
        [pick_x(657), 535],[pick_x(865), 535],[pick_x(1266), 535],[pick_x(1448), 535],[pick_x(1631), 535],[pick_x(1841), 535],
    ]
    mother_text = [
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    mother_entities = [
        'Mother First Name', 'Mother Last Name', 'Mother Birthplace', 'Mother Birthdate', 'Mother ID', "Mother's Father"
    ]
    added = maybe_add_alias(mother, mother_text, [pick_x(1068), 535], 0.35)
    if added:
        mother_entities.append('Mother Alias')
    locs += mother
    locs_text += mother_text
    entities += mother_entities
    father = [
        [pick_x(886), 306],[pick_x(1301), 306],[pick_x(1731), 306],
        [pick_x(657), 565],[pick_x(865), 565],[pick_x(1266), 565],[pick_x(1448), 565],[pick_x(1631), 565],[pick_x(1841), 565],
    ]
    father_text = [
        make_number(), make_number(), make_email(), 
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    father_entities = [
        'Father Mobile Phone', 'Father Home Phone', 'Father Email',
        'Father First Name', 'Father Last Name', 'Father Birthplace', 'Father Birthdate', 'Father ID', "Father's Father"
    ]
    added = maybe_add_alias(father, father_text, [pick_x(1068), 565], 0.35)
    if added:
        father_entities.append('Father Alias')
    locs += father
    locs_text += father_text
    entities += father_entities
    spouse = [
        [pick_x(657), 503],[pick_x(865), 503],[pick_x(1266), 503],[pick_x(1448), 503],[pick_x(1631), 503],[pick_x(1841), 503],
    ]
    spouse_text = [
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    spouse_entities = [
        'Spouse First Name', 'Spouse Last Name', 'Spouse Birthplace', 'Spouse Birthdate', 'Spouse ID', "Spouse's Father"
    ]
    added = maybe_add_alias(spouse, spouse_text, [pick_x(1068), 503], 0.35)
    if added:
        spouse_entities.append('Spouse Alias')
    step_mother = [
        [pick_x(886), 336],[pick_x(1301), 336],[pick_x(1731), 336],
        [pick_x(657), 596],[pick_x(865), 596],[pick_x(1266), 596],[pick_x(1448), 596],[pick_x(1631), 596],[pick_x(1841), 596],
    ]
    step_mother_text = [
        make_number(), make_number(), make_email(),
        make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    step_mother_entities = [
        'Step Mother First Name', 'Step Mother Last Name', 'Step Mother Birthplace', 'Step Mother Birthdate', 'Step Mother ID', "Step Mother's Father"
    ]
    added = maybe_add_alias(step_mother, step_mother_text, [pick_x(1068), 596], 0.35)
    if added:
        step_mother_entities.append('Step Mother Alias')
    step_father = [
        [pick_x(1301), 367],[pick_x(1731), 367],[pick_x(886), 367],
        [pick_x(657), 626],[pick_x(865), 626],[pick_x(1266), 626],[pick_x(1448), 626],[pick_x(1631), 626],[pick_x(1841), 626],
    ]
    step_father_text = [
        make_number(), make_number(), make_email(), make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
    ]
    step_father_entities = [
        'Step Father Mobile Phone', 'Step Father Home Phone', 'Step Father Email'
        'Step Father First Name', 'Step Father Last Name', 'Step Father Birthplace', 'Step Father Birthdate', 'Step Father ID', "Step Father's Father"
    ]
    added = maybe_add_alias(step_father, step_father_text, [pick_x(1068), 626], 0.3)
    if added:
        step_father_entities.append('Step Father Alias')
    u = np.random.uniform()
    sibs = []
    sibs_text = []
    sibs_entities = []
    if u < 0.75:
        sibs += [
            [pick_x(657), 656],[pick_x(865), 656],[pick_x(1266), 656],[pick_x(1448), 656],[pick_x(1631), 656],[pick_x(1841), 656],    
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 1 First Name', 'Sibling 1 Last Name', 'Sibling 1 Birthplace', 'Sibling 1 Birthdate', 'Sibling 1 ID', "Sibling 1 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1068), 656], 0.1)
        if added:
            sibs_entities.append('Sibling 1 Alias')
    if u < 0.55:
        sibs += [
            [pick_x(657), 687],[pick_x(865), 687],[pick_x(1266), 687],[pick_x(1448), 687],[pick_x(1631), 687],[pick_x(1841), 687],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 2 First Name', 'Sibling 2 Last Name', 'Sibling 2 Birthplace', 'Sibling 2 Birthdate', 'Sibling 2 ID', "Sibling 2 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1068), 687], 0.1)
        if added:
            sibs_entities.append('Sibling 2 Alias')
    if u < 0.3:
        sibs += [
            [pick_x(657), 717],[pick_x(865), 717],[pick_x(1266), 717],[pick_x(1448), 717],[pick_x(1631), 717],[pick_x(1841), 717],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 3 First Name', 'Sibling 3 Last Name', 'Sibling 3 Birthplace', 'Sibling 3 Birthdate', 'Sibling 3 ID', "Sibling 3 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1068), 717], 0.1)
        if added:
            sibs_entities.append('Sibling 3 Alias')
    if u < 0.15:
        sibs += [
            [pick_x(657), 748],[pick_x(865), 748],[pick_x(1266), 748],[pick_x(1448), 748],[pick_x(1631), 748],[pick_x(1841), 748],
        ]
        sibs_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        sibs_entities += [
            'Sibling 4 First Name', 'Sibling 4 Last Name', 'Sibling 4 Birthplace', 'Sibling 4 Birthdate', 'Sibling 4 ID', "Sibling 4 Father"
        ]
        added = maybe_add_alias(sibs, sibs_text, [pick_x(1068), 748], 0.1)
        if added:
            sibs_entities.append('Sibling 4 Alias')
    u = np.random.uniform()
    children = []
    children_text = []
    children_entities = []
    if u < 0.4:
        children += [
            [pick_x(657), 779],[pick_x(865), 779],[pick_x(1266), 779],[pick_x(1448), 779],[pick_x(1631), 779],[pick_x(1841), 779],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 1 First Name', 'Child 1 Last Name', 'Child 1 Birthplace', 'Child 1 Birthdate', 'Child 1 ID', "Child 1 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1068), 779], 0.1)
        if added:
            children_entities.append('Child 1 Alias')
    if u < 0.3:
        children += [
            [pick_x(657), 809],[pick_x(865), 809],[pick_x(1266), 809],[pick_x(1448), 809],[pick_x(1631), 809],[pick_x(1841), 809],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 2 First Name', 'Child 2 Last Name', 'Child 2 Birthplace', 'Child 2 Birthdate', 'Child 2 ID', "Child 2 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1068), 809], 0.1)
        if added:
            children_entities.append('Child 2 Alias')
    if u < 0.15:
        children += [
             [pick_x(657), 839],[pick_x(865), 839],[pick_x(1266), 839],[pick_x(1448), 839],[pick_x(1631), 839],[pick_x(1841), 839],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 3 First Name', 'Child 3 Last Name', 'Child 3 Birthplace', 'Child 3 Birthdate', 'Child 3 ID', "Child 3 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1068), 839], 0.1)
        if added:
            children_entities.append('Child 3 Alias')
    if u < 0.05:
        children += [
            [pick_x(657), 869],[pick_x(865), 869],[pick_x(1266), 869],[pick_x(1448), 869],[pick_x(1631), 869],[pick_x(1841), 869],
        ]
        children_text += [
             make_name(), make_name(), make_country(), make_date(), make_number(), make_name()
        ]
        children_entities += [
            'Child 4 First Name', 'Child 4 Last Name', 'Child 4 Birthplace', 'Child 4 Birthdate', 'Child 4 ID', "Child 4 Father"
        ]
        added = maybe_add_alias(children, children_text, [pick_x(1068), 869], 0.1)
        if added:
            children_entities.append('Child 4 Alias')
    u = np.random.uniform()
    countries = []
    countries_text = []
    countries_entities = []
    if u < 0.9:
        countries += [
             [pick_x(424), 1151],[pick_x(796), 1151],[pick_x(1127), 1151],[pick_x(1623), 1151],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 1 Country', 'Travel 1 Start', 'Travel 1 End', 'Travel 1 Names'
        ]
    if u < 0.8:
        countries += [
            [pick_x(424), 1181],[pick_x(796), 1181],[pick_x(1127), 1181],[pick_x(1623), 1181],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 2 Country', 'Travel 2 Start', 'Travel 2 End', 'Travel 2 Names'
        ]
    if u < 0.6:
        countries += [
            [pick_x(424), 1211],[pick_x(796), 1211],[pick_x(1127), 1211],[pick_x(1623), 1211],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 3 Country', 'Travel 3 Start', 'Travel 3 End', 'Travel 3 Names'
        ]
    if u < 0.5:
        countries += [
            [pick_x(424), 1242],[pick_x(796), 1242],[pick_x(1127), 1242],[pick_x(1623), 1242],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 4 Country', 'Travel 4 Start', 'Travel 4 End', 'Travel 4 Names'
        ]
    if u < 0.4:
        countries += [
            [pick_x(424), 1273],[pick_x(796), 1273],[pick_x(1127), 1273],[pick_x(1623), 1273],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 5 Country', 'Travel 5 Start', 'Travel 5 End', 'Travel 5 Names'
        ]
    if u < 0.3:
        countries += [
            [pick_x(424), 1302],[pick_x(796), 1302],[pick_x(1127), 1302],[pick_x(1623), 1302],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 6 Country', 'Travel 6 Start', 'Travel 6 End', 'Travel 6 Names'
        ]
    if u < 0.2:
        countries += [
            [pick_x(424), 1332],[pick_x(796), 1332],[pick_x(1127), 1332],[pick_x(1623), 1332],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 7 Country', 'Travel 7 Start', 'Travel 7 End', 'Travel 7 Names'
        ]
    if u < 0.1:
        countries += [
            [pick_x(424), 1363],[pick_x(796), 1363],[pick_x(1127), 1363],[pick_x(1623), 1363],
        ]
        countries_entities += [
            'Travel 8 Country', 'Travel 8 Start', 'Travel 8 End', 'Travel 8 Names'
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
    if u < 0.05:
        countries += [
            [pick_x(424), 1393],[pick_x(796), 1393],[pick_x(1127), 1393],[pick_x(1623), 1393],
        ]
        countries_text += [
            make_country(), make_date(True), make_date(True), make_name()
        ]
        countries_entities += [
            'Travel 9 Country', 'Travel 9 Start', 'Travel 9 End', 'Travel 9 Names'
        ]
    locs += children
    locs_text += children_text
    entities += children_entities
    locs += sibs
    locs_text += sibs_text
    entities += sibs_entities
    locs += countries
    locs_text += countries_text
    entities += countries_entities
    if np.random.uniform() < 0.3:
        locs += spouse
        locs_text += spouse_text
        entities += spouse_entities
    if np.random.uniform() < 0.15:
        locs += step_mother
        locs_text += step_mother_text
        entities += step_mother_entities
    if np.random.uniform() < 0.15:
        locs += step_father
        locs_text += step_father_text
        entities += step_father_entities
    return np.array(locs) / np.array([2200, 1700]), np.array(locs_text, dtype=object), np.array(entities, dtype=object)