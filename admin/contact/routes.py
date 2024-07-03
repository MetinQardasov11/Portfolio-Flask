from . import contact_bp
from flask import render_template, redirect, url_for, request, flash, session
from models import db
from .forms import ContactForm

@contact_bp.route('/')
def index():
    from models import Contact
    contacts = Contact.query.all()
    return render_template('admin/contact/index.html', contacts=contacts)


@contact_bp.route('/add', methods = ['GET', 'POST'])
def add():
    from models import Contact
    contactForm = ContactForm()
    if request.method == 'POST':
        contact = Contact(
            address = contactForm.address.data,
            phone = contactForm.phone.data,
            email = contactForm.email.data,
            github_link = contactForm.github_link.data,
            linkedin_link = contactForm.linkedin_link.data,
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('admin.contact.index'))
    return render_template('admin/contact/add.html', contactForm=contactForm)


@contact_bp.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    from models import Contact
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.address = request.form['address']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        contact.github_link = request.form['github_link']
        contact.linkedin_link = request.form['linkedin_link']
        db.session.commit()
        return redirect(url_for('admin.contact.index'))
    return render_template('admin/contact/update.html', contact=contact)


@contact_bp.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    from models import Contact
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('admin.contact.index'))