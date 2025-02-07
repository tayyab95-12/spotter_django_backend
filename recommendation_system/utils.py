from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from library.models import Book


def get_recommendations(favorite_books):
    """
    Recommend books based on similarity of favorite books' titles and descriptions.
    """
    # Get all book titles and descriptions
    all_books = Book.objects.exclude(id__in=favorite_books.values_list('id', flat=True))  # Exclude favorites
    if not all_books:
        return []

    # Prepare data for similarity calculation
    favorite_titles = [book.title for book in favorite_books]
    all_titles = [book.title for book in all_books]

    # Use TF-IDF to compute similarity between titles
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(all_titles + favorite_titles)

    # Compute cosine similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Pick top 5 recommendations based on similarity to the favorite list
    recommended_indices = cosine_sim[-len(favorite_titles):, :-len(favorite_titles)].flatten().argsort()[-5:]
    recommended_books = [all_books[int(index)] for index in recommended_indices]

    return recommended_books
