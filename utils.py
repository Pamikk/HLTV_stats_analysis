import csv
ignore_list = ['context-button', 'footer-cta-img', 'button', 'footerlink', 'small-logo', 'dot-menu', 'legacy-stats-section-button', 'col-box', 'sidebar-single-line-item', 'transfer-team-container', 'a-reset', 'dropdown-link', 'nav-link', 'signup-button', 'transfer-player-image-container', 'footer-cta-button', 'deselect', 'responsible-main-text-link', 'stats-top-menu-item']
def test_ignore(item_cls):
    if item_cls is None:
        return False
    item_cls = item_cls[0]
    return True
def save_dict_to_csv(name,data):    
    with open(f'{name}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)