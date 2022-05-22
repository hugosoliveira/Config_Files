set nocompatible              " be iMproved, required
filetype off                  " required

"------------------------------------------------------------------------------------------------------

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Theme for Vim
Plugin 'morhetz/gruvbox'

Plugin 'VundleVim/Vundle.vim'

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
Plugin 'junegunn/vim-easy-align'

"Any valid git URL is allowed
Plugin 'https://github.com/junegunn/vim-github-dashboard.git'

" Multiple Plug commands can be written in a single line using | separators
Plugin 'SirVer/ultisnips' | Plugin 'honza/vim-snippets'

" On-demand loading
Plugin 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plugin 'tpope/vim-fireplace', { 'for': 'clojure' }

" Using a non-default branch
Plugin 'rdnetto/YCM-Generator', { 'branch': 'stable' }

" Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
Plugin 'fatih/vim-go', { 'tag': '*' }

" Plugin options
Plugin 'nsf/gocode', { 'tag': 'v.20150303', 'rtp': 'vim' }

" Plugin outside ~/.vim/plugged with post-update hook
Plugin 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

" A light and configurable statusline/tabline plugin for Vim
" Plugin 'itchyny/lightline.vim'

"Power Line - A better Status line
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

" Latex for Vim
Plugin 'lervag/vimtex'

" Fold the classes correctly
Plugin 'tmhedberg/SimpylFold'

"Fix the Problems with autoIdentation in Python
Plugin 'vim-scripts/indentpython.vim'

"Complete the code
"Plugin 'Valloric/YouCompleteMe'

" Syntax Highlithing
Plugin 'vim-syntastic/syntastic'

" PEP8
Plugin 'nvie/vim-flake8'

"Tabs for NerdTree
Plugin 'jistr/vim-nerdtree-tabs'

"Search Things in from VIM
Plugin 'ctrlpvim/ctrlp.vim'

" Languagetool
Plugin 'dpelle/vim-LanguageTool' 

" Icons for Vim
Plugin 'ryanoasis/vim-devicons'

"Creation of aliases
Plugin 'Konfekt/vim-alias'

" Initialize plugin system
call vundle#end()
filetype plugin on  

"---------------------------------------------
" Configuration for Latex.

function! Writer ()
setlocal spell spelllang=en_us
setlocal formatoptions=jt1
setlocal textwidth=80
setlocal noautoindent
setlocal shiftwidth=5
setlocal tabstop=5
setlocal expandtab

:hi SpellBad ctermfg=15 ctermbg=88 guifg=#FFFFFF guibg=#800000
:hi SpellCap ctermfg=231 ctermbg=31 guifg=#ffffff guibg=#0087af
:hi SpellRare ctermfg=241 ctermbg=252 guifg=#606060 guibg=#d0d0d0
:hi LanguageToolGrammarError ctermfg=0 ctermbg=14 guifg=#FFFFFF guibg=#00ffff
:hi LanguageToolSpellingError term=standout ctermfg=0 ctermbg=11 guifg=Blue guibg=Yellow

endfunction

let g:languagetool_jar='$HOME/Applications/LanguageTool-5.7/languagetool-commandline.jar'
let g:Languagetool_lang='en_US'

com! WR call Writer()

let g:vimtex_view_method = 'zathura'
let g:vimtex_compiler_method = 'latexmk'
let maplocalleader = ","

" settings for sumatraPDF
let g:vimtex_view_general_viewer = 'zathura'
let g:vimtex_view_general_options
    \ = '-reuse-instance -forward-search @tex @line @pdf'
" let g:vimtex_view_general_options_latexmk = '-reuse-instance'

"-----------------------------------------------------------------
set laststatus=2

" Configuration Vim-devIcons
set encoding=UTF-8

" Choosing Font for Vim
set guifont=Fira\ Code:h18

" Configuration for Python

" 1 - Enabling Folding of class/methods
"" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za
"See docstring for folded code
let g:SimpylFold_docstring_preview=1

" PEP 8 Identation
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

" Flag unecessary white spaces
highlight BadWhitespace ctermbg=red guibg=darkred 
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"VirtualEnv Support
"python with virtualenv support

python3 << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
EOF

"Improvement for YCM
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

"Make the Code Look Pretty
let python_highlight_all=1
syntax on

"Ignore files on NERDTREE
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

" Numbers in VIM
set rnu
set number
" Remap
noremap <C-H> <C-W>h
noremap <C-J> <C-W>j
noremap <C-K> <C-W>k
noremap <C-L> <C-W>l
imap jj <ESC>
nnoremap k gk
nnoremap j gj

" Theme for Vim
set bg=dark
autocmd vimenter * ++nested colorscheme gruvbox

" Tab Navigation Config
nnoremap tl :tabnext<CR>
nnoremap th :tabprev<CR>
nnoremap tn :tabnew<CR>
nnoremap tc :tabclose<CR>

" Always show tabline
set showtabline=2

" Highlight line 
set cursorline
